import { Glob } from "bun";

const glob = new Glob("src/**/index.ts");
let entrypoints = [];
for await (const file of glob.scan(".")) {
  entrypoints.push(file);
}
console.log("Building entrypoints:", entrypoints);

// build these files
const result = await Bun.build({
  entrypoints: entrypoints,
  outdir: "build",
  root: "src",
});

const filesBuilt = result.outputs.map((file) => file.path);
console.log("Files built:", filesBuilt);
