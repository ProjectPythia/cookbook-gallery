import { spawn } from "node:child_process";

/**
 * Call out to an external process that conforms to a JSON-based
 * stdin-stdout transform specification.
 *
 * @param opts transform options, containing the binary path and arguments
 */
function externalTransform(opts) {
  return async (mdast) => {
    const data = JSON.stringify(mdast);
    const subprocess = spawn(opts.executable, opts.args ?? []);

    // Pass in the data
    subprocess.stdin.write(data);
    subprocess.stdin.end();

    // Read out the response in chunks
    const stdoutBuffers = [];
    subprocess.stdout.on("data", (chunk) => {
      stdoutBuffers.push(chunk);
    });
    const stderrBuffers = [];
    subprocess.stderr.on("data", (chunk) => {
      stderrBuffers.push(chunk);
    });

    // Await exit
    const exitCode = await new Promise((resolve) => {
      subprocess.on("close", (code) => resolve(code));
    });
    if (exitCode) {
      const stderr = Buffer.concat(stderrBuffers).toString();
      throw new Error(
        `Non-zero error code while running pythia-gallery'\n\n${stderr}`,
      );
    } else if (stderrBuffers.length) {
      const stderr = Buffer.concat(stderrBuffers).toString();
      // Log the error
      console.debug(`\n\n${stderr}\n\n`);
    }
    // Concatenate the responses
    const stdout = Buffer.concat(stdoutBuffers).toString();

    // Modify the tree in-place
    const result = JSON.parse(stdout);
    Object.assign(mdast, result);
  };
}

const cookbooksTransform = () =>
  externalTransform({ executable: "python3", args: ["pythia-gallery.py"] });

const pythiaGalleryDirective = {
  name: "pythia-cookbooks",
  doc: "An example directive for embedding a Pythia cookbook gallery.",
  run() {
    const img = { type: "pythia-cookbooks", children: [] };
    return [img];
  },
};
const pythiaGalleryTransform = {
  plugin: cookbooksTransform,
  stage: "document",
};

const plugin = {
  name: "Pythia Gallery",
  directives: [pythiaGalleryDirective],
  transforms: [pythiaGalleryTransform],
};

export default plugin;
