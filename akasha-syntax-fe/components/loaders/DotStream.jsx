import { useEffect } from "react";

export default function DotStream() {
  useEffect(() => {
    async function getLoader() {
      const { dotStream } = await import("ldrs");
      dotStream.register();
    }
    getLoader();
  }, []);
  return <l-dot-stream size={"50"} speed={"2.5"} color={"hsl(var(--foreground))"} />;
}
