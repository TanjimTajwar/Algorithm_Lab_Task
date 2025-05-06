# Makefile for Simpson's 1/3 Rule Programming Problems

# Variables
JAVA_SRC_DIR = java_solutions
PYTHON_SRC_DIR = python_solutions
JAVA_FILES = $(wildcard $(JAVA_SRC_DIR)/*.java)
PYTHON_FILES = $(wildcard $(PYTHON_SRC_DIR)/*.py)

# Default target
all: compile test

# Compile Java files
compile:
	@echo "Compiling Java files..."
	@javac $(JAVA_FILES)

# Run all Java programs
run-java: compile
	@echo "Running Java programs..."
	@for file in $(JAVA_SRC_DIR)/*.class; do \
		java -cp $(JAVA_SRC_DIR) $$(basename $$file .class); \
	done

# Run all Python programs
run-python:
	@echo "Running Python programs..."
	@for file in $(PYTHON_FILES); do \
		python $$file; \
	done

# Run all programs
run: run-java run-python

# Clean compiled files
clean:
	@echo "Cleaning up..."
	@rm -f $(JAVA_SRC_DIR)/*.class
	@find . -type d -name "__pycache__" -exec rm -rf {} +

# Install Python dependencies
install:
	@echo "Installing Python dependencies..."
	@pip install -r requirements.txt

# Help
help:
	@echo "Available targets:"
	@echo "  all        - Compile and test"
	@echo "  compile    - Compile Java files"
	@echo "  run-java   - Run all Java programs"
	@echo "  run-python - Run all Python programs"
	@echo "  run        - Run all programs"
	@echo "  clean      - Remove compiled files"
	@echo "  install    - Install Python dependencies"
	@echo "  help       - Show this help message"

.PHONY: all compile run-java run-python run clean install help 