---
name: heuristic-evaluation
description: Comprehensive heuristic evaluation workflow for UI/UX interfaces using established usability principles (Nielsen's heuristics, Shneiderman's rules, WCAG guidelines). Use this skill when users ask to conduct heuristic evaluation, usability assessment, expert review, or UI/UX analysis of websites, applications, prototypes, or interfaces. Supports two modes - virtual expert mode for quick design feedback, and expert review mode for generating evaluation forms. Generates structured Excel reports with findings, severity ratings, and actionable recommendations.
---

# Heuristic Evaluation

A comprehensive workflow for conducting usability heuristic evaluations of digital interfaces.

## Usage Modes

### Mode 1: Virtual Expert (Quick Evaluation)

Fast evaluation by Claude acting as a virtual UX expert.

**When to use:**
- Project timelines are tight
- No access to UX experts
- Need quick feedback on design mockups or prototypes
- Want to identify critical issues before user testing

**How it works:**
- Ask Claude to evaluate your interface (provide URL or upload designs)
- Claude performs static analysis automatically (page structure, forms, navigation, accessibility basics)
- Claude guides you through interactive testing (error handling, user control, feedback mechanisms)
- Claude documents findings with heuristic violations, severity ratings, and recommendations
- Claude automatically generates Excel evaluation report

---

### Mode 2: Provide Evaluation Template

Provide task-oriented evaluation template for human experts to complete.

**When to use:**
- Have time and resources for formal expert review
- Need assessment from multiple experts (3-5 recommended)
- Want comprehensive evaluation with detailed documentation
- Require professional audit trail

**How it works:**
- Request evaluation template from Claude
- Claude provides pre-built Excel template from assets
- Define task flow based on evaluation scope (template includes common examples: e-commerce, SaaS, content sites)
- Fill in product information in Instructions sheet
- Distribute template to experts
- Experts perform tasks and record findings (task, violated heuristic, description, screenshot, severity)
- Collect completed forms and consolidate findings
- Hold debriefing session to discuss, prioritize, and plan actions

---

## Heuristic Evaluation Principles

These principles integrate Nielsen's Usability Heuristics and Shneiderman's Golden Rules, representing universal usability best practices.

### 1. Visibility of System Status

**Principle:** Keep users informed about what is going on through appropriate feedback within reasonable time.

**Check for:**
- Loading indicators for async operations
- Progress bars for multi-step processes
- Confirmation messages after actions
- Current location indicators (breadcrumbs, active states)
- System state visibility (selected items, applied filters)

**Common Issues:**
- No feedback after button clicks
- Missing loading states
- Unclear current location
- Silent failures

---

### 2. Match Between System and Real World

**Principle:** Use language, concepts, and conventions familiar to users, not system-oriented terms.

**Check for:**
- Plain language (no jargon or technical terms)
- Familiar icons and metaphors
- Natural information order
- Domain-appropriate terminology

**Common Issues:**
- Technical error codes without explanation
- Unfamiliar icons without labels
- System terminology instead of user terminology

---

### 3. User Control and Freedom

**Principle:** Provide clearly marked exits and easy reversal of actions to relieve anxiety and encourage exploration.

**Check for:**
- Undo/redo functionality
- Cancel buttons at every step
- Easy backward navigation
- Clear exit paths from dialogs
- Ability to recover from errors

**Common Issues:**
- Irreversible destructive actions
- No way to go back without losing data
- Forced completion of flows
- Hard-to-find cancel options

---

### 4. Consistency and Standards

**Principle:** Maintain consistency in sequences, terminology, visual design, and behavior throughout the interface.

**Check for:**
- Consistent terminology across all screens
- Uniform visual styling (colors, fonts, spacing)
- Predictable control behavior
- Platform convention adherence
- Consistent action sequences

**Common Issues:**
- Different terms for same concept
- Inconsistent button placement
- Varying interaction patterns
- Mixed visual styles

---

### 5. Error Prevention

**Principle:** Prevent errors before they occur; if errors happen, provide simple recovery paths.

**Check for:**
- Input validation and constraints
- Disabled states for unavailable actions
- Confirmation for destructive actions
- Smart defaults
- Helpful suggestions (autocomplete, format hints)

**Error Types:**
- **Slips** (unconscious): Prevent with constraints, formatting
- **Mistakes** (conscious but wrong): Prevent with clear info, confirmations

**Common Issues:**
- No input validation
- Missing confirmation for delete
- Unclear action consequences
- No constraints on invalid input

---

### 6. Recognition Rather Than Recall

**Principle:** Minimize memory load by making elements, actions, and options visible. Recognition is easier than recall.

**Check for:**
- Visible navigation and options
- Clear labels on all controls
- Recently used items accessible
- Context preserved across pages
- Information visible when needed

**Common Issues:**
- Hidden navigation requiring memorization
- Unlabeled icons
- Multi-step forms requiring remembering previous info
- Information needed but not displayed

---

### 7. Flexibility and Efficiency

**Principle:** Accommodate both novice and expert users with appropriate features for each.

**Check for:**
- Keyboard shortcuts for power users
- Customizable workflows
- Bulk actions for repeated tasks
- Quick access to frequent functions
- Progressive disclosure of advanced features

**Common Issues:**
- No shortcuts for common actions
- Cannot customize interface
- All users forced through same slow process
- Advanced features buried too deep

---

### 8. Aesthetic and Minimalist Design

**Principle:** Interfaces should contain only relevant information. Every extra element competes with relevant elements.

**Check for:**
- Clear visual hierarchy
- Important content stands out
- No unnecessary elements
- Effective use of white space
- Focused on user tasks

**Common Issues:**
- Cluttered interfaces
- Competing visual elements
- Unnecessary decorations
- Information overload
- Poor visual hierarchy

---

### 9. Help Users Recognize, Diagnose, and Recover from Errors

**Principle:** Error messages should clearly explain the problem and constructively suggest solutions.

**Check for:**
- Plain language error messages (no codes)
- Specific problem identification
- Constructive solutions offered
- Friendly, empathetic tone
- Easy error recovery

**Good Error Messages Include:**
- What went wrong (specific)
- Why it happened (when helpful)
- How to fix it (actionable steps)

**Common Issues:**
- Generic "Error" messages
- Technical error codes without explanation
- Blame-focused language ("You did...")
- No guidance on next steps

---

### 10. Help and Documentation

**Principle:** Systems should be usable without documentation, but provide help when needed.

**Check for:**
- Easy-to-find help resources
- Contextual help (tooltips, inline hints)
- Searchable documentation
- Task-focused tutorials
- Onboarding for new users

**Common Issues:**
- No help available
- Help difficult to find
- Documentation not searchable
- Help doesn't match current version

---

### 11. Offer Informative Feedback

**Principle:** Every user action should receive appropriate interface feedback. Scale feedback to action significance.

**Check for:**
- Immediate feedback for all actions
- Subtle feedback for minor/frequent actions
- Substantial feedback for major/infrequent actions
- Visual presentation of changes

**Common Issues:**
- No feedback after actions
- Same feedback for all actions
- Delayed confirmations
- Invisible state changes

---

### 12. Design Dialogs to Yield Closure

**Principle:** Organize action sequences with clear beginning, middle, and end. Provide satisfying completion feedback.

**Check for:**
- Clear task boundaries
- Defined steps in multi-step processes
- Completion confirmations
- Progress indicators
- Final confirmation screens

**Common Issues:**
- Unclear task boundaries
- Missing completion confirmations
- Ambiguous process endpoints
- No sense of progress

---

### 13. Seek Universal Usability

**Principle:** Design for diverse users considering expertise, age, disabilities, international variations, and technology diversity.

**Check for:**
- Features for novices (explanations, help)
- Features for experts (shortcuts, customization)
- Accessibility features (see WCAG section below)
- Internationalization support
- Responsive design for different devices

**Common Issues:**
- Single user persona assumed
- No accessibility considerations
- Expert-only or novice-only design
- No device adaptation

---

## WCAG Quick Accessibility Check

Basic accessibility checks to identify critical issues:

### Perceivable
- [ ] **Alt text**: All images have descriptive alt text
- [ ] **Color contrast**: Text meets 4.5:1 ratio (3:1 for large text)
- [ ] **Color not sole indicator**: Information not conveyed by color alone
- [ ] **Text resize**: Content readable when text scaled to 200%

### Operable
- [ ] **Keyboard accessible**: All functionality available via keyboard
- [ ] **No keyboard trap**: Users can navigate away from any element
- [ ] **Focus visible**: Clear focus indicator for keyboard navigation
- [ ] **Touch targets**: Minimum 44×44 CSS pixels for touch targets

### Understandable
- [ ] **Language identified**: Page language specified in HTML
- [ ] **Labels present**: All form inputs have labels
- [ ] **Error identification**: Errors clearly identified and described
- [ ] **Instructions provided**: Complex inputs have instructions

### Robust
- [ ] **Valid HTML**: Proper nesting, unique IDs, valid attributes
- [ ] **ARIA used correctly**: ARIA attributes complement, not replace, HTML semantics
- [ ] **Name, role, value**: UI components properly identified for assistive tech

**For detailed WCAG reference, see `references/wcag-detailed.md`**

---

## Common Anti-Patterns to Avoid

Quick identification of problematic design patterns:

### Dark Patterns (Manipulative Design)
- **Disguised ads**: Ads disguised as content or navigation
- **Forced continuity**: Charging after free trial without clear warning
- **Hidden costs**: Surprise fees at checkout
- **Confirm shaming**: Guilt-tripping users who decline
- **Misdirection**: Highlighting one choice while hiding better option

### Usability Anti-Patterns
- **Mystery meat navigation**: Unlabeled icons
- **Pagination abuse**: Excessive pagination for content
- **Auto-playing media**: Video/audio starts without user action
- **Modal overload**: Too many modal dialogs disrupting flow
- **Captive data**: No export functionality
- **Forced registration**: Requiring account for browsing

### Form Anti-Patterns
- **Premature validation**: Showing errors before user finished typing
- **CAPTCHA abuse**: Overly difficult or frequent CAPTCHAs
- **Unclear requirements**: Password rules shown only after error
- **Lost data on error**: Form cleared when validation fails
- **Disabled paste**: Preventing paste in password fields

---

## Severity Rating Guidelines

**Critical:**
- Prevents task completion
- Causes data loss
- Severe accessibility violations (WCAG A)
- Legal or compliance risk
- Security vulnerability

**High:**
- Major usability problems
- Significant user confusion
- Workflow disruption
- Important feature unusable
- WCAG AA violations

**Medium:**
- Noticeable issues that slow users
- Minor confusion
- Inconsistency issues
- Suboptimal but functional

**Low:**
- Minor inconsistencies
- Cosmetic issues
- Opportunities for improvement
- Nice-to-have enhancements

---

## Priority Assignment

- **P0:** Critical severity + blocks core user flow
- **P1:** High severity + affects main user flows
- **P2:** Medium severity + affects secondary features
- **P3:** Low severity + enhancement opportunities

---

## Best Practices

**During Evaluation:**
- Focus on one principle at a time
- Test with realistic user tasks
- Document positive examples too
- Consider context-specific factors
- Look for patterns across screens

**When Reporting:**
- Be specific about problem and location
- Explain user impact, not just violation
- Provide actionable recommendations
- Group related issues
- Prioritize by severity and impact

**Communication:**
- Use clear, non-technical language
- Include screenshots when helpful
- Acknowledge design constraints
- Present findings constructively

---

## Resources

### references/wcag-detailed.md

WCAG 2.1/2.2 knowledge reference for identifying accessibility issues and providing recommendations.

**When to use:**
- Need to understand specific WCAG standards and requirements
- Identifying accessibility violations during evaluation
- Want to provide specific, standards-based recommendations
- Need to assess severity of accessibility issues
- Explaining why something is an accessibility problem

**Contains:**
- Complete WCAG 2.1/2.2 guidelines organized by principle (Perceivable, Operable, Understandable, Robust)
- Conformance levels (A, AA, AAA) with requirements
- Common violations and what to look for
- Good practices for accessible design
- Severity assessment guidelines for accessibility issues
- Quick wins (high impact, low effort improvements)
- Key principles for making recommendations

### scripts/invoke_virtual_expert.py

Invokes virtual expert to generate evaluation report in Evaluation Form format.

**When to use:**
- After completing Virtual Expert Mode evaluation
- Have collected all findings with heuristic violations, severity ratings, and recommendations
- Ready to create final deliverable report

**Automatically executed by Claude** to produce:
- Evaluation Form sheet with columns: Task, Violated Heuristic, Description (includes recommendation), Screenshot, Severity
- Color-coded severity levels with softer colors for better readability
- Dropdown validations for consistency
- All Task entries in bold font

**Report format matches expert evaluation template** for easy handoff or further review.

### assets/evaluation-template.xlsx

Task-oriented evaluation template for expert evaluation.

**When to use:**
- User requests evaluation template for expert review
- Setting up formal expert review process
- Need standardized evaluation form for multiple experts

**Provide directly to user when requested.** Template includes:
- Instructions sheet with task flow planning (includes examples: e-commerce, SaaS, content sites)
- Evaluation form with columns: Task, Violated Heuristic, Description, Screenshot, Severity

User defines task flow based on their product, then experts record findings while performing each task. Screenshots can be pasted directly in cells or attached separately. Priority is determined later during team planning and ticketing.
