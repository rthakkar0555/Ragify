import type { Metadata } from "next";
import "@/styles/globals.css";

export const metadata: Metadata = {
  title: "RAGify | Illuminated Intelligence",
  description:
    "POST your data. GET intelligent answers. RAGify is a modular RAG-as-a-Service platform that handles retrieval infrastructure for AI applications.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark" suppressHydrationWarning>
      <body className="min-h-screen font-geist antialiased">{children}</body>
    </html>
  );
}
