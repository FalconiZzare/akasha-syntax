import { clsx } from "clsx";
import { twMerge } from "tailwind-merge";
import { toast } from "sonner";
import { CheckCircle, TriangleAlert } from "lucide-react";

export function cn(...inputs) {
  return twMerge(clsx(inputs));
}

export const triggerToast = (message, status = "success", description) => {
  if (status === "error") {
    toast.error(message, {
      description: description,
      icon: <TriangleAlert className={"h-4 w-4 text-red-500"} />,
      className: "border-destructive"
    });
  } else {
    toast(message, {
      description: description,
      icon: <CheckCircle className={"h-4 w-4 text-green-500"} />
    });
  }
};
