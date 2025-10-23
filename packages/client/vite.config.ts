import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { fileURLToPath } from "node:url";

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),

      "@atoms": fileURLToPath(
        new URL("./src/components/atoms", import.meta.url)
      ),
      "@molecules": fileURLToPath(
        new URL("./src/components/molecules", import.meta.url)
      ),
      "@organisms": fileURLToPath(
        new URL("./src/components/organisms", import.meta.url)
      ),
      "@templates": fileURLToPath(
        new URL("./src/components/templates", import.meta.url)
      ),
      "@pages": fileURLToPath(
        new URL("./src/components/pages", import.meta.url)
      ),
      "@guards": fileURLToPath(new URL("./src/router/guards", import.meta.url)),
      "@store": fileURLToPath(new URL("./src/store", import.meta.url)),
      "@api": fileURLToPath(new URL("./src/api", import.meta.url)),
      "@hooks": fileURLToPath(new URL("./src/hooks", import.meta.url)),
      "@validation": fileURLToPath(
        new URL("./src/validation", import.meta.url)
      ),
      "@validations": fileURLToPath(
        new URL("../server/src/validations", import.meta.url)
      ),
      "@styles": fileURLToPath(new URL("./src/styles", import.meta.url)),
    },
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData:
          '@use "@/styles/variables" as *;\n@use "@/styles/mixins" as *;\n@use "@/styles/responsive" as *;\n',
      },
    },
  },
});
