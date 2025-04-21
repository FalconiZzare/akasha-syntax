"use client";

import React, { useState } from "react";
import Wrapper from "@/components/Wrapper";
import { Send, CornerDownLeft, LoaderCircle } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import Sphere from "@/components/Sphere";
import { cn, triggerToast } from "@/lib/utils";
import { useMutation } from "@tanstack/react-query";
import { ask } from "@/services/syntax";
import DotStream from "@/components/loaders/DotStream";

const Page = () => {
  const [inputValue, setInputValue] = useState("");
  const [responses, setResponses] = useState([]);

  const { isPending, mutate, reset } = useMutation({
    mutationKey: ["chat"],
    mutationFn: async () => {
      const data = new FormData();
      data.append("query", inputValue);

      return await ask(data);
    },
    onSuccess: (data) => {
      const newRes = [...responses];

      newRes.push({ text: data.data.response, type: "response" });

      setResponses(newRes);
      setInputValue("");
    },
    onError: (error) => {
      triggerToast(error.message || "There was an error", "error");
      console.log(error);
    }
  });

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const newRes = [...responses];
    newRes.push({ text: inputValue, type: "query" });
    setResponses(newRes);

    await reset();
    await mutate();
  };

  return (
    <Wrapper className={"mt-20"}>
      <div className="flex h-full items-start justify-center">
        <div className="h-full w-full overflow-hidden rounded-lg shadow-lg">
          <div className="h-full overflow-y-auto px-4">
            <div className="mb-16 flex flex-col items-center justify-center">
              <div className={"flex items-center justify-center"}>
                <Sphere className={"w-[250px]"} />
              </div>
              <p className="text-center text-2xl font-medium capitalize text-accent-foreground">
                How can I help?
              </p>
            </div>

            <div className="mt-10 flex flex-col space-y-3 pb-20">
              {responses.length > 0 ? (
                responses.map((item, index) => (
                  <div key={index} className={"flex w-full flex-col items-end space-y-3"}>
                    <p
                      className={cn(
                        "w-max max-w-sm break-words rounded-lg border px-4 py-2 text-sm shadow-sm",
                        item.type === "query" ? "bg-accent" : "self-start"
                      )}
                    >
                      {item.text}
                    </p>
                  </div>
                ))
              ) : (
                <p className={"self-center text-center font-medium tracking-wide"}>
                  You can start with asking something related to JavaScript, Python, Java or C++
                </p>
              )}
              {isPending && (
                <div className={cn("max-w-sm px-4 py-2 text-sm shadow-sm", "self-start")}>
                  <DotStream />
                </div>
              )}
            </div>
          </div>
        </div>

        <div className="fixed bottom-0 left-0 right-0 rounded-xl border-t bg-background p-4">
          <form onSubmit={handleSubmit} className="relative">
            <Input
              type="text"
              placeholder="Ask me something..."
              value={inputValue}
              onChange={handleInputChange}
              className="rounded-full py-3 pl-4 pr-20 focus-visible:ring-secondary"
              disabled={isPending}
            />
            <div className="absolute right-2 top-1/2 flex -translate-y-1/2 transform items-center">
              {inputValue ? (
                isPending ? (
                  <Button
                    disabled={isPending}
                    type="submit"
                    size="icon"
                    variant="ghost"
                    className="h-8 w-8 rounded-full"
                  >
                    <LoaderCircle className="mt-1 animate-spin text-accent-foreground" />
                  </Button>
                ) : (
                  <Button
                    disabled={isPending}
                    type="submit"
                    size="icon"
                    variant="ghost"
                    className="h-8 w-8 rounded-full"
                  >
                    <CornerDownLeft className="h-5 w-5 text-accent-foreground" />
                  </Button>
                )
              ) : (
                <Button
                  disabled={isPending}
                  type="submit"
                  size="icon"
                  variant="ghost"
                  className="h-8 w-8 rounded-full"
                >
                  <Send className="mt-1 text-accent-foreground" />
                </Button>
              )}
            </div>
          </form>
        </div>
      </div>
    </Wrapper>
  );
};

export default Page;
