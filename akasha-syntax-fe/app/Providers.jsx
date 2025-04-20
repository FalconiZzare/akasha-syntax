"use client";

import React from "react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { AppProgressProvider as ProgressProvider } from "@bprogress/next";

const queryClient = new QueryClient();

const Providers = ({ children }) => {
  return (
    <QueryClientProvider client={queryClient}>
      <ProgressProvider
        height={"3px"}
        color={"hsl(var(--primary))"}
        options={{ showSpinner: false }}
        shallowRouting
      >
        {children}
      </ProgressProvider>
    </QueryClientProvider>
  );
};

export default Providers;
