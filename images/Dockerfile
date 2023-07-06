# Base image
FROM openjdk:11

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Build the project
RUN ./gradlew build

# Set the entrypoint
ENTRYPOINT ["java", "-jar", "build/libs/terraform2023-1.0.jar"]
