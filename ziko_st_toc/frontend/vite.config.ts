import process from "node:process";
import { defineConfig, UserConfig } from "vite";

/**
 * Vite configuration for Streamlit Custom Component v2 development (no React).
 */
export default defineConfig(() => {
  const isProd = process.env.NODE_ENV === "production";
  const isDev = !isProd;

  return {
    base: "./",

    define: {
      "process.env.NODE_ENV": JSON.stringify(process.env.NODE_ENV),
    },

    build: {
      minify: isDev ? false : "esbuild",
      outDir: "build",
      sourcemap: isDev,

      // // ✅ IMPORTANT: inline everything for Streamlit v2
      // cssCodeSplit: false,

      // rollupOptions: {
      //   output: {
      //     // ✅ ensures single JS file (no chunks)
      //     inlineDynamicImports: true,
      //   },
      // },

      lib: {
        entry: "./src/index.js",
        name: "MyComponent",
        formats: ["es"],
        fileName: "index-[hash]",
      },

      ...(!isDev && {
        esbuild: {
          drop: ["console", "debugger"],
          minifyIdentifiers: true,
          minifySyntax: true,
          minifyWhitespace: true,
        },
      }),
    },
  } satisfies UserConfig;
});