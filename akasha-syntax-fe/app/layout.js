import { Poppins } from "next/font/google";
import "./globals.css";
import Providers from "@/app/Providers";
import Navbar from "@/components/Layout/Navbar";

const poppins = Poppins({
  subsets: ["latin"],
  weight: ["100", "200", "300", "400", "500", "600", "700", "800", "900"]
});

export const metadata = {
  title: "Akasha Syntax",
  description:
    "Akasha Syntax is a Retrieval-Augmented Generation (RAG) system that processes code issues and documentation to provide intelligent, context-aware answers to developer queries."
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={`${poppins.className} antialiased`}>
        <Providers>
          <div className={"grid min-h-dvh grid-rows-[1fr_auto]"}>
            <Navbar />
            {children}
          </div>
        </Providers>
      </body>
    </html>
  );
}
