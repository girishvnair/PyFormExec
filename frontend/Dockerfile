# Use Node.js image
FROM node:16-alpine as build

# Set working directory
WORKDIR /app

# Copy the frontend code
COPY ./frontend /app

# Install dependencies and build the app
RUN npm install && npm run build

# Serve the built app with a static server
FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
