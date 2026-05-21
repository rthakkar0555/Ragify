FROM node:20-alpine AS base

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json* ./
RUN npm ci

COPY frontend/ .
RUN npm run build

FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV=production

COPY --from=base /app/.next/standalone ./
COPY --from=base /app/.next/static ./.next/static

# Copy public directory if it exists (optional for Next.js apps)
RUN mkdir -p ./public
COPY --from=base /app/public ./public || true

EXPOSE 3000

CMD ["node", "server.js"]
