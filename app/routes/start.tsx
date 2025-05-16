import type { MetaFunction } from "@remix-run/node";
import MultiStep from "~/Components/MultiStep";
import Heading from "~/Components/Elements/Heading";

export const meta: MetaFunction = () => {
  return [
    { title: "UseCase Assistant" },
    { name: "description", content: "UseCase Assistant" },
  ];
};

export default function Index() {
  return (
    <div className="flex flex-col h-screen bg-[url('https://flowbite.s3.amazonaws.com/docs/jumbotron/hero-pattern.svg')]">
      <div className="flex justify-center mt-10">
        <Heading />
      </div>
      <div className="flex flex-grow items-center justify-center">
        <MultiStep />
      </div>
    </div>
  );
}
