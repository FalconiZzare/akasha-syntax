import React from "react";
import { cn } from "@/lib/utils";

const Sphere = ({ className }) => {
  return (
    <div className={cn("flex h-[150px] w-[450px] items-center justify-center", className)}>
      <div
        className={"pointer-events-none overflow-clip"}
        style={{
          WebkitMaskImage: "radial-gradient(50% 50% at 50% 50%, #fff 10.94%, transparent 100%)",
          maskImage: "radial-gradient(50% 50% at 50% 50%, #fff 10.94%, transparent 100%)",
          maskSize: "cover",
          WebkitMaskSize: "cover"
        }}
      >
        <div className={"h-auto w-full"}>
          <video
            preload={"false"}
            muted
            playsInline
            autoPlay
            loop
            src={"/videos/original-sphere.mp4"}
            className={"-z-50 overflow-clip"}
          />
        </div>
      </div>
    </div>
  );
};

export default Sphere;
