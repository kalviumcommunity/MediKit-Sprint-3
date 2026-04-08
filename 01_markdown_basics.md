# Markdown Basics for Data Science Notebooks

## Introduction
This document demonstrates fundamental Markdown syntax used in Jupyter Notebooks and documentation files.
Markdown is essential for creating readable, well-documented data science projects.

## Headings
Headings are created using hash symbols (#). The number of hashes determines the heading level.

# Heading Level 1
## Heading Level 2
### Heading Level 3
#### Heading Level 4
##### Heading Level 5

## Lists

### Unordered Lists
Use dashes, asterisks, or plus signs to create bullet points:

- First item
- Second item
- Third item
  - Nested item 1
  - Nested item 2
- Fourth item

### Ordered Lists
Use numbers followed by periods to create numbered lists:

1. First step
2. Second step
3. Third step
   1. Sub-step A
   2. Sub-step B
4. Fourth step

### Mixed Lists
You can combine ordered and unordered lists:

- Data preparation
  1. Load data
  2. Clean data
- Data analysis
  1. Exploratory analysis
  2. Statistical testing
- Visualization
  1. Create plots
  2. Generate reports

## Code Blocks

### Inline Code
Use single backticks for inline code: `print("Hello, World!")` or `import pandas as pd`.

### Code Block - Python
Use triple backticks with language specification:

```python
import numpy as np
import pandas as pd

# Load sample data
data = np.array([1, 2, 3, 4, 5])
print("Data shape:", data.shape)
```

### Code Block - SQL
```sql
SELECT * FROM users WHERE age > 18;
```

### Code Block - Plain Text
```
This is plain text code block
No syntax highlighting applied
```

## Text Formatting

**Bold text** is created with double asterisks
*Italic text* is created with single asterisks
***Bold and italic*** uses triple asterisks
~~Strikethrough~~ uses double tildes

## Blockquotes
> This is a blockquote
> It can span multiple lines
> Great for highlighting important information

> Point 1
> - Nested list in quote
> - Another point

## Horizontal Line
---

## Links and Images

[Link to Google](https://www.google.com)
[Link to local file](./README.md)

## Tables

| Feature | Description | Usage |
|---------|-------------|-------|
| Bold | Strong emphasis | **text** |
| Italic | Emphasis | *text* |
| Code | Inline code | `code` |
| Links | Reference URLs | [text](url) |

## Tips and Best Practices

1. Use clear, descriptive headings
2. Break content into logical sections
3. Use code blocks for examples
4. Include tables for comparing information
5. Add links to related resources
6. Keep formatting consistent

## Summary
Markdown allows you to create well-structured, readable documentation that integrates seamlessly
with Jupyter Notebooks and version control systems.
