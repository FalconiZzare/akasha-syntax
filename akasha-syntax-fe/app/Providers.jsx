"use client";

import React from "react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { AppProgressProvider as ProgressProvider } from "@bprogress/next";
import { ThemeProvider } from "@/components/ThemeProvider";

const queryClient = new QueryClient();

const Providers = ({ children }) => {
  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider attribute={"class"} defaultTheme={"dark"}>
        <ProgressProvider
          height={"3px"}
          color={"hsl(var(--primary))"}
          options={{ showSpinner: false }}
          shallowRouting
        >
          {children}
        </ProgressProvider>
      </ThemeProvider>
    </QueryClientProvider>
  );
};

export default Providers;
