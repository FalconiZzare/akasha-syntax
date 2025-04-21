import Sphere from "@/components/Sphere";
import Wrapper from "@/components/Wrapper";
import StarBorder from "@/components/ui/starborder";
import { Bot, BotMessageSquare, ChevronRight } from "lucide-react";
import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <Wrapper className={"mt-20"}>
      <div className={"relative flex h-full flex-col items-center justify-center"}>
        <StarBorder>
          <div className={"flex w-full items-center justify-between gap-4"}>
            <div
              className={
                "rounded-full border-2 border-foreground/50 bg-gradient-to-b from-primary via-primary to-secondary px-1 py-[3px]"
              }
            >
              <Bot className={"mb-px"} size={20} />
            </div>
            AI Code Help
          </div>
        </StarBorder>
        <h1
          className={
            "mt-6 bg-gradient-to-b from-neutral-800 via-white to-white bg-clip-text text-center text-2xl font-medium text-transparent sm:text-4xl md:text-6xl"
          }
        >
          Get Personalized Code Help <br />
          <span className={"mt-2 block"}>with Akasha Syntax</span>
        </h1>
        <div className={"mt-16 flex items-center justify-center"}>
          <Sphere />
        </div>

        <div className={"mt-20 text-center"}>
          <Button
            variant={"outline"}
            className={
              "gap-6 rounded-full border-foreground/30 bg-background/30 px-[6px] py-[26px] shadow-lg backdrop-blur-lg hover:bg-background/50 [&_svg]:size-7"
            }
          >
            <div
              className={
                "rounded-full border-2 border-foreground/50 bg-gradient-to-b from-primary via-primary to-secondary px-1 py-[3px]"
              }
            >
              <BotMessageSquare className={"mb-px"} size={26} />
            </div>
            <p className={"text-xl font-normal"}>Try Akasha Syntax</p>
            <div className={"flex"}>
              <ChevronRight />
              <ChevronRight className={"-ml-4 text-foreground/70"} />
              <ChevronRight className={"-ml-4 text-foreground/50"} />
            </div>
          </Button>
        </div>
      </div>

      <div
        className={
          "absolute inset-0 left-1/2 top-1/2 -z-10 size-[300px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-gradient-to-b from-primary via-primary to-secondary opacity-25 blur-3xl md:size-[550px] lg:size-[650px] lg:opacity-15"
        }
      />
    </Wrapper>
  );
}
