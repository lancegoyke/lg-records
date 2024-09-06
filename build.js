import { Glob } from "bun";

const glob = new Glob("src/**/*.ts");

for await (const file of glob.scan(".")) {
  console.log(file); // => "index.ts"
}
