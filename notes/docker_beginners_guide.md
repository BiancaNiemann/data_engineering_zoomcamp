# Docker Beginner's Guide (Codespaces Edition)

## What is Docker?

Docker is a platform that lets you package applications and their dependencies into **containers**. Think of containers as lightweight, portable boxes that contain everything your application needs to run (code, libraries, system tools, settings).

### Why use Docker?

- **Consistency**: "Works on my machine" → "Works everywhere"
- **Isolation**: Each container runs independently
- **Portability**: Run the same container on your laptop, server, or cloud
- **Efficiency**: Faster and lighter than virtual machines

---

## Docker in Codespaces

Good news! Docker is **pre-installed** in GitHub Codespaces, so you can start using it immediately without any setup. Just open your terminal and you're ready to go!

✅ **Codespaces advantages**:
- Docker already installed and configured
- No need to install Docker Desktop
- Works the same way as on your local machine
- Can build and run containers directly

---

## Core Concepts

### 1. **Images**
A blueprint or template for a container. Like a recipe that describes what goes into your container.

```
┌─────────────────────┐
│   Docker Image      │  (Read-only template)
│                     │
│  ┌───────────────┐  │
│  │ Your App      │  │
│  ├───────────────┤  │
│  │ Dependencies  │  │
│  ├───────────────┤  │
│  │ OS Libraries  │  │
│  └───────────────┘  │
└─────────────────────┘
```

### 2. **Containers**
A running instance of an image. Like a dish made from a recipe.

```
   Image                    Container
┌─────────┐              ┌─────────────┐
│ Recipe  │  ─────────>  │ Running App │
│ (nginx) │    docker    │  (isolated) │
└─────────┘     run      └─────────────┘
```

### 3. **Dockerfile**
A text file with instructions to build a Docker image. Like writing your own recipe.

```dockerfile
FROM node:18          # Start with Node.js
COPY . /app           # Copy your code
RUN npm install       # Install dependencies
CMD ["npm", "start"]  # Run the app
```

### 4. **Docker Hub**
A registry where you can find and share Docker images. Like GitHub for Docker images.

---

## The Docker Workflow

```
┌──────────────┐
│  Write a     │  Create Dockerfile
│  Dockerfile  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ docker build │  Build an image from Dockerfile
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  docker run  │  Create and start a container
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Container   │  Your app is running!
│   Running    │
└──────────────┘
```

---

## Essential Commands

### Image Commands

#### `docker pull`
**What it does**: Downloads an image from Docker Hub

```bash
docker pull nginx
docker pull node:18
docker pull python:3.11
```

**Example**:
```bash
# Pull the latest nginx image
docker pull nginx:latest
```

---

#### `docker images` or `docker image ls`
**What it does**: Lists all images on your system

```bash
docker images
```

**Example output**:
```
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
nginx         latest    a6bd71f48f68   2 weeks ago    187MB
node          18        3b9d0d9a0b1c   3 weeks ago    993MB
```

---

#### `docker build`
**What it does**: Builds an image from a Dockerfile

```bash
docker build -t my-app:v1 .
```

- `-t` = tag (name) your image
- `.` = build context (current directory)

**Example**:
```bash
# Build image named "my-node-app" with tag "latest"
docker build -t my-node-app:latest .
```

---

#### `docker rmi`
**What it does**: Removes an image

```bash
docker rmi nginx
docker rmi my-app:v1
```

**Force remove**:
```bash
docker rmi -f my-app:v1
```

---

### Container Commands

#### `docker run`
**What it does**: Creates and starts a container from an image

```bash
docker run [OPTIONS] IMAGE [COMMAND]
```

**Common options**:
- `-d` = detached mode (run in background)
- `-p` = port mapping (host:container)
- `--name` = give container a name
- `-e` = set environment variables
- `-v` = mount volumes
- `--rm` = automatically remove container when it stops

**Examples**:
```bash
# Run nginx in background, map port 8080 to 80
docker run -d -p 8080:80 --name my-nginx nginx

# Run and interact with Ubuntu shell
docker run -it ubuntu bash

# Run with environment variable
docker run -e MY_VAR=hello my-app

# Run and auto-remove when stopped
docker run --rm my-app
```

---

#### `docker ps`
**What it does**: Lists running containers

```bash
docker ps           # Running containers only
docker ps -a        # All containers (including stopped)
```

**Example output**:
```
CONTAINER ID   IMAGE   COMMAND                  PORTS                  NAMES
a1b2c3d4e5f6   nginx   "nginx -g 'daemon of…"   0.0.0.0:8080->80/tcp   my-nginx
```

---

#### `docker stop`
**What it does**: Stops a running container

```bash
docker stop my-nginx
docker stop a1b2c3d4e5f6  # By container ID
```

---

#### `docker start`
**What it does**: Starts a stopped container

```bash
docker start my-nginx
```

---

#### `docker restart`
**What it does**: Restarts a container

```bash
docker restart my-nginx
```

---

#### `docker rm`
**What it does**: Removes a stopped container

```bash
docker rm my-nginx
docker rm $(docker ps -aq)  # Remove all stopped containers
```

**Force remove running container**:
```bash
docker rm -f my-nginx
```

---

#### `docker exec`
**What it does**: Runs a command in a running container

```bash
docker exec [OPTIONS] CONTAINER COMMAND
```

**Examples**:
```bash
# Open a bash shell in running container
docker exec -it my-nginx bash

# Run a single command
docker exec my-nginx ls /usr/share/nginx/html

# Check logs inside container
docker exec my-nginx cat /var/log/nginx/access.log
```

---

#### `docker logs`
**What it does**: Shows logs from a container

```bash
docker logs my-nginx
docker logs -f my-nginx     # Follow logs (like tail -f)
docker logs --tail 50 my-nginx  # Last 50 lines
```

---

#### `docker inspect`
**What it does**: Shows detailed information about a container or image

```bash
docker inspect my-nginx
docker inspect nginx
```

---

### Utility Commands

#### `docker system df`
**What it does**: Shows Docker disk usage

```bash
docker system df
```

---

#### `docker system prune`
**What it does**: Cleans up unused Docker resources

```bash
docker system prune       # Remove stopped containers, unused networks, dangling images
docker system prune -a    # Remove ALL unused images too
docker system prune --volumes  # Also remove unused volumes
```

**⚠️ Tip for Codespaces**: Regularly run this to save disk space!

---

## Creating Your First Dockerfile

### Simple Node.js Example

**Dockerfile**:
```dockerfile
# Start from official Node.js image
FROM node:18

# Set working directory inside container
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy application code
COPY . .

# Expose port 3000
EXPOSE 3000

# Command to run the app
CMD ["node", "app.js"]
```

**Build and run**:
```bash
# Build the image
docker build -t my-node-app .

# Run the container
docker run -d -p 3000:3000 --name my-app my-node-app

# Check logs
docker logs my-app

# Stop and remove
docker stop my-app
docker rm my-app
```

---

### Simple Python Example

**Dockerfile**:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

---

### Simple Static Website (nginx)

**Dockerfile**:
```dockerfile
FROM nginx:alpine

# Copy your HTML files to nginx directory
COPY ./html /usr/share/nginx/html

EXPOSE 80
```

**Build and run**:
```bash
docker build -t my-website .
docker run -d -p 8080:80 my-website
```

Then in Codespaces, you can forward port 8080 to view your site!

---

## Port Forwarding in Codespaces

When you run a container with exposed ports in Codespaces, GitHub will automatically detect them and offer to forward them.

**Example**:
```bash
# Run nginx on port 8080
docker run -d -p 8080:80 nginx
```

Codespaces will show a notification to open port 8080. Click it or:
1. Go to the **Ports** tab in Codespaces
2. Your port should appear automatically
3. Click the globe icon to open in browser

---

## Docker Compose Basics

Docker Compose lets you define multi-container applications in a `docker-compose.yml` file.

**docker-compose.yml**:
```yaml
version: '3.8'

services:
  web:
    image: nginx
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html

  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
```

**Commands**:
```bash
docker-compose up        # Start all services
docker-compose up -d     # Start in background
docker-compose down      # Stop and remove all services
docker-compose ps        # List running services
docker-compose logs      # View logs
docker-compose logs -f   # Follow logs
```

---

## Common Dockerfile Instructions

| Instruction | Purpose | Example |
|-------------|---------|---------|
| `FROM` | Base image to start from | `FROM node:18` |
| `WORKDIR` | Set working directory | `WORKDIR /app` |
| `COPY` | Copy files from host to container | `COPY . /app` |
| `ADD` | Like COPY but can extract archives | `ADD archive.tar.gz /app` |
| `RUN` | Execute commands during build | `RUN npm install` |
| `CMD` | Default command when container starts | `CMD ["node", "app.js"]` |
| `ENTRYPOINT` | Command that always runs | `ENTRYPOINT ["python"]` |
| `EXPOSE` | Document which ports are used | `EXPOSE 3000` |
| `ENV` | Set environment variables | `ENV NODE_ENV=production` |
| `VOLUME` | Create mount point for volumes | `VOLUME /data` |

---

## Practical Examples

### Example 1: Run a Quick Web Server

```bash
# Run nginx and serve current directory
docker run -d -p 8080:80 -v $(pwd):/usr/share/nginx/html nginx
```

### Example 2: Run a Database

```bash
# Run PostgreSQL
docker run -d \
  --name my-postgres \
  -e POSTGRES_PASSWORD=mysecretpass \
  -p 5432:5432 \
  postgres

# Connect to it
docker exec -it my-postgres psql -U postgres
```

### Example 3: Run Redis

```bash
# Run Redis
docker run -d --name my-redis -p 6379:6379 redis

# Check if it's working
docker exec -it my-redis redis-cli ping
# Should return: PONG
```

---

## Understanding Layers

Docker images are built in layers. Each instruction in a Dockerfile creates a new layer.

```
┌─────────────────────┐
│ CMD ["npm","start"] │  Layer 4: Command
├─────────────────────┤
│ COPY . .            │  Layer 3: App code
├─────────────────────┤
│ RUN npm install     │  Layer 2: Dependencies
├─────────────────────┤
│ FROM node:18        │  Layer 1: Base image
└─────────────────────┘
```

**Why it matters**:
- Layers are cached
- Put things that change least at the top
- Put things that change most at the bottom

**Good example**:
```dockerfile
FROM node:18
WORKDIR /app
COPY package*.json ./    # Copy dependencies first
RUN npm install          # This layer is cached if package.json doesn't change
COPY . .                 # Copy code last (changes often)
```

---

## Best Practices

### ✅ Do's
- Use official images as base when possible
- Use specific tags instead of `latest` (e.g., `node:18` not `node:latest`)
- Use `.dockerignore` to exclude unnecessary files
- Keep images small (use alpine variants when possible)
- One process per container
- Use multi-stage builds for smaller production images

### ❌ Don'ts
- Don't store secrets in Dockerfiles or images
- Don't run containers as root when possible
- Don't install unnecessary packages
- Don't use `latest` tag in production
- Don't put large files in your image

---

## .dockerignore Example

Create a `.dockerignore` file to exclude files from the build context:

```
node_modules
npm-debug.log
.git
.gitignore
README.md
.env
.DS_Store
*.log
```

---

## Multi-Stage Build Example

Reduces final image size by only including what's needed to run:

```dockerfile
# Build stage
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Production stage
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY package*.json ./
RUN npm install --production
CMD ["node", "dist/app.js"]
```

---

## Troubleshooting Tips

### Container exits immediately
Check the logs:
```bash
docker logs my-container
```

### Can't connect to exposed port
Make sure port mapping is correct:
```bash
docker ps  # Check PORTS column
```

In Codespaces, check the Ports tab!

### "Address already in use"
Another container is using that port:
```bash
docker ps  # Find the container
docker stop <container-name>
```

### Remove all containers and start fresh
```bash
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker system prune -a
```

### Out of disk space in Codespaces
```bash
docker system prune -a --volumes
```

---

## Quick Reference Card

| Command | Purpose |
|---------|---------|
| `docker pull <image>` | Download an image |
| `docker images` | List images |
| `docker build -t <name> .` | Build image from Dockerfile |
| `docker run -d -p 8080:80 <image>` | Run container in background |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker stop <container>` | Stop a container |
| `docker start <container>` | Start a container |
| `docker rm <container>` | Remove a container |
| `docker rmi <image>` | Remove an image |
| `docker logs <container>` | View logs |
| `docker exec -it <container> bash` | Access container shell |
| `docker system prune -a` | Clean up everything |

---

## Getting Help

- Official docs: https://docs.docker.com
- Docker Hub: https://hub.docker.com
- Use `docker --help` or `docker <command> --help`
- In Codespaces: Docker is already configured and ready!

---

## Next Steps

1. **Try running some popular images**: nginx, postgres, redis, mongo
2. **Create your first Dockerfile**: Package a simple app
3. **Learn Docker Compose**: Manage multi-container applications
4. **Explore Docker Hub**: Find useful images for your projects
5. **Practice in Codespaces**: Perfect environment for learning!

---

**Happy Dockering! 🐳**