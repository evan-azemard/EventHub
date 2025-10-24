FROM node:20-alpine

WORKDIR /app

# Installer de pnpm
RUN npm install -g pnpm

# Copie les fichier de config de monorépo
COPY pnpm-workspace.yaml pnpm-lock.yaml package.json ./

# Copie les packages
COPY packages/server ./packages/server

# Installe les dépendances
RUN pnpm install --frozen-lockfile

# Build le server
WORKDIR /app/packages/server
RUN pnpm run build

EXPOSE 8000

CMD ["node", "dist/server.js"]
