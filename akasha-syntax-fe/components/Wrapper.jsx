import React from "react";
import { cn } from "@/lib/utils";

const Wrapper = ({ className, children }) => {
  return <div className={cn("w-full px-3 py-2", className)}>{children}</div>;
};

export default Wrapper;
