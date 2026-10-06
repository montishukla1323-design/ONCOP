# ==============================================================================
# ONCOP - One Nation One Complaint Portal Docker Containerfile
# Base: Node.js 22 LTS Alpine (includes native node:sqlite)
# ==============================================================================

FROM node:22-alpine AS base

# Install wget for healthcheck
RUN apk add --no-cache tzdata wget

ENV NODE_ENV=production
ENV PORT=3000
ENV HOST=0.0.0.0

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci --only=production --ignore-scripts

# Copy application source code
COPY . .

# Ensure storage directories exist with appropriate permissions
RUN mkdir -p /app/uploads && chown -R node:node /app

# Switch to non-root user for container security
USER node

# Expose HTTP port
EXPOSE 3000

# Docker Healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD wget -qO- http://127.0.0.1:3000/api/health || exit 1

# Start ONCOP production server
CMD ["node", "server.js"]
