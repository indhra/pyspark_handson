# Copilot Instructions for PySpark Hands-On Project

## Project Overview
This is a PySpark hands-on learning and experimentation workspace focused on distributed data processing and analytics. The project emphasizes practical implementations and educational examples.

## Development Environment

### Spark Setup
- Use PySpark for all Spark operations
- Default to local Spark mode for development: `spark = SparkSession.builder.appName("app_name").master("local[*]").getOrCreate()`
- Include proper Spark session cleanup with `spark.stop()` in examples
- Configure Spark with appropriate memory settings for local development

### Python Environment
- Follow PEP 8 style guidelines for Python code
- Use type hints for function signatures when dealing with Spark DataFrames and RDDs
- Import PySpark modules explicitly: `from pyspark.sql import SparkSession, DataFrame`
- Use `pyspark.sql.functions` for DataFrame operations rather than raw SQL when possible

## Code Organization Patterns

### Notebook Structure
- Start notebooks with environment setup and Spark session initialization
- Include clear markdown sections explaining concepts before code blocks
- End notebooks with cleanup section stopping Spark session
- Use descriptive variable names that indicate data types (e.g., `df_sales`, `rdd_logs`)

### Data Processing Patterns
- Prefer DataFrame API over RDD API for structured data
- Use `.cache()` or `.persist()` for DataFrames accessed multiple times
- Always include `.show()` or `.collect()` examples to demonstrate results
- Handle schema explicitly when reading data: use `.schema()` parameter

### File Organization
- Create separate directories for different learning topics (e.g., `/basics/`, `/ml/`, `/streaming/`)
- Keep sample datasets in `/data/` directory
- Store utility functions in `/utils/` for reuse across notebooks
- Include requirements.txt or environment.yml for dependency management

## Common Operations

### Data Reading Examples
```python
# CSV with schema
df = spark.read.option("header", "true").schema(schema).csv("path/to/file.csv")

# Parquet (preferred for Spark)
df = spark.read.parquet("path/to/file.parquet")
```

### Performance Considerations
- Use `.explain()` to understand query plans in learning examples
- Demonstrate partitioning concepts with `.repartition()` and `.coalesce()`
- Show broadcast joins for small dimension tables
- Include examples of avoiding shuffles where possible

## Testing Approach
- Create simple unit tests using pytest for custom functions
- Use `spark.createDataFrame()` for creating test datasets
- Include data validation examples using DataFrame operations
- Test both happy path and edge cases (empty DataFrames, null values)

## Documentation Standards
- Include docstrings for all custom functions with parameter types
- Add inline comments explaining Spark-specific operations and optimizations
- Document performance implications of different approaches
- Provide links to official Spark documentation for complex operations

## Learning Resources Integration
- Include references to Spark UI (localhost:4040) for job monitoring
- Document how to access Spark logs for debugging
- Provide examples that demonstrate Spark's lazy evaluation
- Show both imperative and functional programming approaches where applicable