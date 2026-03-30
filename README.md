# Octal Calculator - Team Development Standards

This document outlines coding standards and workflows for the 5-member development team to ensure seamless collaboration with minimal merge conflicts.

---

## 1. Module Ownership & File Structure

Each team member owns a specific module with a dedicated file. **Do not edit files outside your assigned module** except during integration review.

| Member | Role | Module | File | Responsibility |
|--------|------|--------|------|-----------------|
| Member 1 | Parser | Input Parsing + Base Tag Handling | `parser.py` | Parse `O'247`, `D'123` format; extract mode prefix; normalize input |
| Member 2 | Validator | Input Validation Engine | `validator.py` | Validate octal/decimal characters; check format; error reporting |
| Member 3 | Converter | Octal ↔ Decimal Conversion | `converter.py` | Convert `O'247` ↔ `D'167`; preserve output format |
| Member 4 | Arithmetic | Octal Arithmetic + Complements | `arithmetic.py` | Add/subtract/multiply/divide in octal; 7's & 8's complements |
| Member 5 | Integration | Integration + E2E Testing | `calculator.py`, `test_calculator.py` | Wire all modules; orchestrate workflow; end-to-end testing |

---

## 2. Branch & Commit Naming Conventions

**Branch naming:**
```
feature/member<N>-<module-name>
example: feature/member1-parser, feature/member2-validator
```

**Commit message format:**
```
[ModuleName] Brief description

[Parser] Add base prefix detection for O' and D'
[Validator] Validate octal characters (0-7 only)
[Converter] Implement octal to decimal conversion
[Arithmetic] Add octal addition operation
[Integration] Wire parser to validator
```

Keep commit messages focused on **one logical change per commit**.

---

## 3. Code Style & Consistency

### Python Style Guide
- **Indentation:** 4 spaces (not tabs)
- **Line length:** Max 100 characters
- **Naming conventions:**
  - Functions/variables: `snake_case` (e.g., `parse_input`, `validate_octal`)
  - Classes: `PascalCase` (e.g., `OctalParser`)
  - Constants: `UPPER_SNAKE_CASE`
- **Type hints:** Use Python type annotations for all function parameters and return types
  ```python
  def parse_input(input_str: str) -> dict:
  ```
- **Docstrings:** Use Google-style docstrings
  ```python
  def convert_octal_to_decimal(octal_value: str) -> str:
      """Converts octal value to decimal.
      
      Args:
          octal_value: String in format "O'247"
      
      Returns:
          Decimal string in format "D'167"
      """
  ```

---

## 4. Function & Class Interfaces (Contracts)

**Define & lock interfaces early.** Each module exports specific functions that downstream modules depend on. Do not change signatures without coordinating with dependent modules.

### Member 1 - Parser Output Contract
```python
def parse_input(input_str: str) -> dict:
    """
    Returns: {
        'base_mode': 'OCT' | 'DEC',
        'value': str,
        'is_valid': bool,
        'error': str | None
    }
    """
```

### Member 2 - Validator Output Contract
```python
def validate_input(parsed: dict) -> dict:
    """
    Returns: {
        'is_valid': bool,
        'error_message': str | None,
        'error_type': 'INVALID_CHAR' | 'FORMAT_ERROR' | None
    }
    """
```

### Member 3 - Converter Output Contract
```python
def convert(value: str, from_base: str, to_base: str) -> str:
    """
    Args:
        value: numeric string (no prefix)
        from_base: 'OCT' or 'DEC'
        to_base: 'OCT' or 'DEC'
    
    Returns: Converted value with prefix (e.g., "O'247" or "D'167")
    """
```

### Member 4 - Arithmetic Output Contract
```python
def octal_add(operand1: str, operand2: str) -> str:
    """Both operands assumed to be octal values (without prefix)."""
    
def get_complement(value: str, complement_type: int) -> str:
    """complement_type: 7 or 8"""
```

---

## 5. Testing Standards

### Unit Tests (Each Member)
- Create `test_<module>.py` for your module
- Test **only your module's functions** in isolation
- Name tests descriptively: `test_parse_octal_input`, `test_validate_invalid_char`
- Aim for >80% code coverage within your module

**Example:**
```python
# test_parser.py
import unittest
from parser import parse_input

class TestParser(unittest.TestCase):
    def test_parse_octal_with_prefix(self):
        result = parse_input("O'247")
        self.assertEqual(result['base_mode'], 'OCT')
        self.assertEqual(result['value'], '247')
```

### Integration Tests (Member 5)
- Create `test_calculator.py` (end-to-end workflows)
- Test complete flows: `parse → validate → convert → arithmetic`
- Example: `"O'247" + "O'15" = "O'264"`

---

## 6. Import & Dependency Rules

**Dependency Flow:**
```
Calculator (Member 5)
    ↓
Parser (Member 1) → Validator (Member 2) → Converter (Member 3) → Arithmetic (Member 4)
```

**Rules:**
- Member 1 imports: Only standard library
- Member 2 imports: `parser` (from Member 1)
- Member 3 imports: `parser`, `validator` (from Members 1, 2)
- Member 4 imports: Only standard library
- Member 5 imports: All other modules

**No circular imports allowed.** If you find yourself needing to import from a downstream module, refactor to extract common logic into a shared utility.

---

## 7. Pull Request & Merge Workflow

### Individual PRs (Members 1-4)
1. Create feature branch: `feature/member<N>-<module>`
2. Commit changes with tagged messages
3. Open PR with title: `[Member N] <Module Name> Implementation`
4. PR description should include:
   - Functions implemented
   - Test coverage
   - Any interface changes (if applicable)
5. Require code review from Member 5 (Integration Lead)

### Integration PR (Member 5)
1. After all 4 modules merged to `main`, Member 5 creates integration branch
2. Wire modules together in `calculator.py`
3. Run all integration tests
4. Open final PR: `[Integration] Octal Calculator E2E Implementation`

---

## 8. Conflict Prevention Checklist

**Before pushing, verify:**
- [ ] You've only edited your assigned module file(s)
- [ ] Your function signatures match the agreed contracts (Section 4)
- [ ] Your imports follow the dependency rules (Section 6)
- [ ] You've added unit tests for your code
- [ ] You've run your tests locally and they pass
- [ ] Your commit message follows the format in Section 2
- [ ] You haven't modified other members' files

---

## 9. Communication & Coordination

- **Slack/Chat channel:** Use for quick questions about interfaces
- **Weekly sync:** 10 min standup before each PR submission
- **Interface changes:** Announce in channel immediately; update this README Section 4
- **Blockers:** If waiting on another module, notify in chat; Member 5 can create mock interfaces temporarily

---

## 10. Version Control Basics

```bash
# Create your feature branch (do this first)
git checkout main
git pull origin main
git checkout -b feature/member1-parser

# Make changes, commit frequently
git add <your-files>
git commit -m "[Parser] Add base prefix detection"

# Push and create PR
git push origin feature/member1-parser
```

---

## Quick Reference

| Task | Owner | File | Interface |
|------|-------|------|-----------|
| Parse `O'247` | Member 1 | `parser.py` | `parse_input()` |
| Validate characters | Member 2 | `validator.py` | `validate_input()` |
| `O'247` → `D'167` | Member 3 | `converter.py` | `convert()` |
| `O'247` + `O'15` | Member 4 | `arithmetic.py` | `octal_add()`, `get_complement()` |
| Orchestrate all | Member 5 | `calculator.py` + tests | `main()` |

---

**Last Updated:** [Date]  
**Maintained By:** Integration Team  
**Questions?** Contact Member 5 (Integration Lead)
