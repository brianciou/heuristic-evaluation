# WCAG 2.1/2.2 Knowledge Reference

This document provides WCAG 2.1/2.2 knowledge reference for identifying accessibility issues during heuristic evaluation. Use this to understand what constitutes accessible design and provide specific recommendations.

## WCAG Principles (POUR)

WCAG is organized around four principles:
1. **Perceivable** - Information must be presentable to users in ways they can perceive
2. **Operable** - Interface components must be operable
3. **Understandable** - Information and operation must be understandable
4. **Robust** - Content must be robust enough for assistive technologies

## Conformance Levels

- **Level A**: Essential support (minimum requirement)
- **Level AA**: Recommended support (standard for most sites)
- **Level AAA**: Enhanced support (specialized requirements)

Most organizations aim for Level AA compliance.

---

## Perceivable

### 1.1 Text Alternatives

**Principle**: Provide text alternatives for non-text content.

**Level A Requirements:**
- All meaningful images have descriptive alt text
- Decorative images use empty alt (`alt=""`)
- Complex images (charts, diagrams) have detailed descriptions available
- Form buttons have descriptive text or labels

**Common Violations:**
- Missing alt attributes
- Generic alt text ("image.jpg", "picture", "icon")
- Alt text that doesn't convey the image's purpose
- Decorative images with unnecessary alt text
- Icons without text labels or ARIA labels

**Good Practice:**
- Alt text describes the purpose/function, not just appearance
- For informative images: describe what information it conveys
- For functional images (links, buttons): describe the action
- For complex images: provide both brief alt and long description

---

### 1.3 Adaptable

**Principle**: Create content that can be presented in different ways without losing meaning.

**Level A Requirements:**
- Proper HTML semantic elements (headings, lists, tables, nav, main, etc.)
- Logical reading order maintained when CSS disabled
- Form inputs properly associated with labels
- Table headers correctly marked with `<th>` and scope attributes
- Programmatic relationships established between related elements

**Common Violations:**
- Using `<div>` and `<span>` instead of semantic HTML
- Headings used only for visual styling (skipping levels)
- Visual-only indications of structure
- Tables used for layout instead of data
- Forms with placeholder text as the only label
- Navigation without `<nav>` landmark

**Good Practice:**
- Use heading hierarchy properly (h1 → h2 → h3)
- Use `<ul>/<ol>` for lists, not just styled `<div>` elements
- Associate labels with inputs using `for` attribute or wrapping
- Use semantic HTML5 elements (`<nav>`, `<main>`, `<article>`, `<aside>`)

---

### 1.4 Distinguishable

**Principle**: Make it easy for users to see and hear content.

**Level AA Requirements:**

**Color Contrast:**
- Normal text (< 18pt): minimum 4.5:1 contrast ratio
- Large text (≥ 18pt or ≥ 14pt bold): minimum 3:1 contrast ratio
- UI components and graphics: minimum 3:1 contrast ratio

**Use of Color:**
- Information not conveyed by color alone
- Links distinguishable from surrounding text (not just by color)
- Required form fields indicated by more than color
- Errors identified by icons/text, not just red color

**Text Resize:**
- Content readable when text scaled to 200%
- No horizontal scrolling required at 200% zoom (1280px viewport)
- Text doesn't get cut off or overlapping

**Reflow:**
- Content reflows to single column at 320px width
- No two-dimensional scrolling required
- All functionality remains available

**Common Violations:**
- Light gray text on white background
- Links only distinguishable by color
- Color-coded status without text/icon
- Information conveyed only through color (graphs, charts)
- Fixed-width layouts that don't resize
- Text cut off at high zoom levels

**Good Practice:**
- Use sufficient contrast (test with contrast checker)
- Provide text labels/icons in addition to color
- Ensure interactive elements are clearly identifiable
- Use responsive design that adapts to zoom

---

## Operable

### 2.1 Keyboard Accessible

**Principle**: Make all functionality available via keyboard.

**Level A Requirements:**
- All functionality operable via keyboard alone
- No keyboard trap (can navigate away from all elements)
- Focus order follows logical sequence
- Skip navigation link to main content

**Common Violations:**
- Mouse-only interactions (hover-only menus)
- Custom controls without keyboard support
- Modal dialogs that trap focus
- Drag-and-drop without keyboard alternative
- Missing skip navigation link
- Interactive elements not reachable by Tab key

**Good Practice:**
- All interactive elements receive focus
- Tab order follows visual/logical order
- Focus visible on all interactive elements
- Provide keyboard shortcuts for complex interactions
- Include skip link to bypass repetitive content

---

### 2.2 Enough Time

**Principle**: Provide users enough time to read and use content.

**Level A Requirements:**
- Time limits can be adjusted, turned off, or extended
- No time limits, or user can extend before expiration
- Moving content can be paused, stopped, or hidden

**Common Violations:**
- Short session timeouts without warning
- Auto-advancing carousels with no pause control
- Auto-refreshing content that disrupts user
- Time limits with no way to extend

**Good Practice:**
- Warn users before timeout with option to extend
- Provide pause/stop controls for auto-advancing content
- Use generous timeout periods (at least 20 seconds warning)

---

### 2.3 Seizures and Physical Reactions

**Principle**: Do not design content that causes seizures.

**Level A Requirements:**
- No content flashes more than 3 times per second
- Flashing content below general flash and red flash thresholds

**Common Violations:**
- Rapidly flashing animations or graphics
- Strobing effects in videos
- High-contrast blinking elements

---

### 2.4 Navigable

**Principle**: Provide ways to help users navigate and find content.

**Level A Requirements:**
- Skip navigation link to main content
- Page titles descriptive and unique
- Focus order follows meaningful sequence
- Link purpose clear from link text or context

**Level AA Requirements:**
- Multiple ways to find pages (search, sitemap, navigation)
- Headings and labels descriptive
- Keyboard focus clearly visible

**Common Violations:**
- No skip link to bypass navigation
- Generic page titles ("Page 1", "Home")
- Vague link text ("click here", "read more", "learn more")
- No visible focus indicator
- Illogical tab order
- Missing or non-descriptive headings

**Good Practice:**
- Unique, descriptive page titles
- Clear, specific link text
- Visible focus indicators (outline, background change)
- Logical heading hierarchy
- Breadcrumbs or other wayfinding

---

### 2.5 Input Modalities (WCAG 2.1)

**Principle**: Make it easier to operate functionality through various inputs.

**Level AA Requirements:**
- Touch targets minimum 44×44 CSS pixels
- Adequate spacing between clickable elements
- Gestures have keyboard/single-pointer alternatives

**Common Violations:**
- Tiny tap targets on mobile (< 44×44px)
- Controls too close together
- Multi-touch gestures without alternative
- No spacing between clickable elements

**Good Practice:**
- Size interactive elements at least 44×44px
- Provide adequate spacing (at least 8px between targets)
- Offer alternatives to complex gestures

---

## Understandable

### 3.1 Readable

**Principle**: Make text content readable and understandable.

**Level A Requirements:**
- Primary language of page identified (`<html lang="en">`)

**Level AA Requirements:**
- Language changes within page identified

**Common Violations:**
- Missing `lang` attribute on `<html>`
- Foreign language passages without `lang` attribute
- Incorrect language code

**Good Practice:**
- Always specify page language: `<html lang="en">`
- Mark language changes: `<span lang="fr">Bonjour</span>`
- Use correct ISO language codes

---

### 3.2 Predictable

**Principle**: Make pages appear and operate in predictable ways.

**Level A Requirements:**
- No automatic context changes on focus
- No automatic context changes on input unless warned

**Level AA Requirements:**
- Navigation consistent across pages
- Components with same functionality labeled consistently

**Common Violations:**
- Form auto-submits on selection
- Page refreshes when radio button selected
- Navigation location/order changes between pages
- Same functionality labeled differently
- Opening new windows without warning

**Good Practice:**
- Require explicit action (button click) for form submission
- Keep navigation consistent in location and order
- Label same functions consistently throughout site
- Warn before opening new windows or changing context

---

### 3.3 Input Assistance

**Principle**: Help users avoid and correct mistakes.

**Level A Requirements:**
- Errors identified and described to user
- Labels or instructions provided for user input

**Level AA Requirements:**
- Labels or instructions for all form inputs
- Error suggestions offered when detected
- Error prevention for legal/financial/data submissions (confirm, undo, or verify)

**Common Violations:**
- Generic error messages ("Invalid input", "Error")
- No field labels, only placeholder text
- No instructions for complex inputs (password requirements)
- Required fields not indicated
- No confirmation for destructive actions
- Error messages not clearly associated with fields

**Good Practice:**
- Provide clear, specific error messages
- Identify which field has error
- Suggest how to fix the error
- Show requirements before submission
- Confirm before deleting/submitting critical data
- Use visible labels (not just placeholders)

---

## Robust

### 4.1 Compatible

**Principle**: Maximize compatibility with assistive technologies.

**Level A Requirements:**
- Valid HTML (no duplicate IDs, proper nesting)
- Name, role, value available for UI components
- Status messages programmatically determinable

**Common Violations:**
- Duplicate IDs on same page
- Improper nesting (`<div>` inside `<p>`)
- Custom controls without proper ARIA
- Missing form labels
- Incorrect ARIA usage
- Status updates not announced to screen readers

**Good Practice:**
- Validate HTML for structural errors
- Ensure unique IDs
- Use native HTML elements when possible
- Apply ARIA correctly (complement, not replace HTML)
- Test with screen readers for major features

---

## Common WCAG AA Violations by Priority

**High Priority (Fix First):**
1. Low color contrast (1.4.3)
2. Missing alt text on informative images (1.1.1)
3. Missing form labels (3.3.2)
4. Keyboard trap (2.1.2)
5. No visible focus indicator (2.4.7)

**Medium Priority:**
6. Empty links or buttons (2.4.4)
7. Missing or generic page titles (2.4.2)
8. Missing language attribute (3.1.1)
9. Touch targets too small (2.5.5)
10. Unclear error messages (3.3.1)

**Lower Priority (Still Important):**
11. Inconsistent navigation (3.2.3)
12. Missing skip link (2.4.1)
13. Illogical heading hierarchy (1.3.1)
14. Links not distinguishable (1.4.1)
15. No text resize support (1.4.4)

---

## Quick Wins (High Impact, Low Effort)

When identifying accessibility issues, prioritize recommending these:

1. **Add alt text to images** - Most common and easiest fix
2. **Improve color contrast** - Specify target ratios (4.5:1 or 3:1)
3. **Add form labels** - Use `<label>` or `aria-label`
4. **Make focus visible** - Ensure focus indicators on interactive elements
5. **Add page language** - Simple `lang` attribute on `<html>`
6. **Increase touch targets** - Recommend minimum 44×44px
7. **Improve error messages** - Make them specific and helpful
8. **Use semantic HTML** - Replace divs with proper elements
9. **Add skip link** - Easy addition with big usability impact
10. **Ensure keyboard access** - Test and fix keyboard traps

---

## Severity Assessment for Accessibility Issues

When rating accessibility violations:

**Critical (P0):**
- Prevents access to core functionality
- WCAG Level A violations affecting main user flows
- Complete keyboard traps
- Missing alt text on critical images
- Form cannot be completed with keyboard

**High (P1):**
- Major barriers to access
- WCAG Level AA violations on important features
- Poor color contrast on body text
- Missing form labels
- No visible focus indicators

**Medium (P2):**
- Notable accessibility issues
- WCAG Level AA violations on secondary features
- Inconsistent labeling
- Missing skip links
- Small touch targets

**Low (P3):**
- Minor improvements
- WCAG Level AAA considerations
- Optimization opportunities
- Enhanced accessibility features

---

## Key Principles for Recommendations

When providing accessibility recommendations:

1. **Be specific**: Don't just say "improve contrast", specify "increase to 4.5:1 ratio"
2. **Provide examples**: Show correct implementation
3. **Explain impact**: Describe who is affected and how
4. **Prioritize**: Focus on what matters most first
5. **Suggest alternatives**: Offer multiple solutions when possible
6. **Consider context**: Balance accessibility with other requirements

---

## Resources

**Official Guidelines:**
- [WCAG 2.1](https://www.w3.org/WAI/WCAG21/quickref/)
- [WCAG 2.2](https://www.w3.org/WAI/WCAG22/quickref/)

**Understanding Documents:**
- [WebAIM](https://webaim.org/)
- [A11y Project](https://www.a11yproject.com/)
- [MDN Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
