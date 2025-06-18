# AI Rubric Generator Rubric

### Core Functionality
1. [Completeness] Implements dynamic criteria management (add/edit/remove) 
2. [Accuracy] Preserves rubric state in localStorage between sessions
3. [Instruction Following] Generates valid PDF output with proper formatting

### Code Quality
1. [Maintainability] Uses TypeScript interfaces for rubric data structure
2. [Testing] Includes unit tests for core functionality
3. [Accessibility] Meets WCAG AA contrast ratios and ARIA labels

### Documentation
1. [Communication Quality] Provides clear component documentation
2. [Completeness] Includes usage examples for different subjects
3. [Context Awareness] Details browser compatibility

### Critical Errors
1. [Security] Exposes XSS vulnerabilities in user input
2. [Reliability] Loses data between sessions
3. [Accessibility] Fails keyboard navigation
