import React from "react";
import Image from "next/image";
import { Button } from "@/components/ui/button";
import { Sparkles } from "lucide-react";
import Link from "next/link";

const Navbar = () => {
  return (
    <nav
      className={
        "fixed left-0 right-0 top-0 z-50 flex select-none justify-between overflow-hidden bg-background/15 px-2 py-4 backdrop-blur-sm"
      }
    >
      <Link href={"/"}>
        <Image
          src={"/images/akasha-syntax.png"}
          width={300}
          height={0}
          alt={"logo"}
          className={"pointer-events-none -ml-7 select-none"}
        />
      </Link>

      <div className={"rounded-full bg-gradient-to-b from-primary via-primary to-secondary p-px"}>
        <Button className={"rounded-full border-none"} variant={"outline"}>
          <p className={"hidden md:block"}>Try Premium</p>
          <Sparkles />
        </Button>
      </div>
    </nav>
  );
};

export default Navbar;
