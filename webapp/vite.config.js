import { resolve } from 'path'

export default {
  base: '/',
  root: resolve(__dirname, 'src'),
  build: {
    outDir: '../dist',
    assetsDir: 'assets'
  },
  server: {
    port: 8080
  },
  preview: {
    port: 4173
  },
  publicDir: 'resources', // Sets resources as a static folder
  css: {
     preprocessorOptions: {
        scss: {
          silenceDeprecations: [
            'import',
            'mixed-decls',
            'color-functions',
            'global-builtin',
            'if-function'
          ],
        },
     },
  },
}