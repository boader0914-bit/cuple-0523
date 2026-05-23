---
name: Hospitality Precision System
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#45474b'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#75777c'
  outline-variant: '#c5c6cb'
  surface-tint: '#595f69'
  primary: '#02060e'
  on-primary: '#ffffff'
  primary-container: '#191f28'
  on-primary-container: '#818792'
  inverse-primary: '#c1c7d3'
  secondary: '#0059b9'
  on-secondary: '#ffffff'
  secondary-container: '#1071e5'
  on-secondary-container: '#fefcff'
  tertiary: '#00050f'
  on-tertiary: '#ffffff'
  tertiary-container: '#141f2c'
  on-tertiary-container: '#7c8797'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dde3ef'
  primary-fixed-dim: '#c1c7d3'
  on-primary-fixed: '#161c25'
  on-primary-fixed-variant: '#414751'
  secondary-fixed: '#d7e2ff'
  secondary-fixed-dim: '#acc7ff'
  on-secondary-fixed: '#001a40'
  on-secondary-fixed-variant: '#004491'
  tertiary-fixed: '#d8e3f5'
  tertiary-fixed-dim: '#bcc7d9'
  on-tertiary-fixed: '#111c29'
  on-tertiary-fixed-variant: '#3d4856'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  display-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.25'
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-md-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  title-lg:
    fontFamily: Hanken Grotesk
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.5'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Hanken Grotesk
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 20px
  section-gap-lg: 120px
  section-gap-sm: 64px
---

## Brand & Style
The design system is rooted in the philosophy of "Essential Precision." It balances high-level structural diagnosis with surgical execution. Designed for hospitality owners and B2B stakeholders, the visual language avoids the consumer-facing "vacation" aesthetic in favor of a **Corporate Modern** style that feels authoritative yet approachable.

The personality is field-oriented—valuing practical results over abstract theory. The UI utilizes expansive whitespace, rigorous grid alignment, and a "restrained premium" feel that communicates trustworthiness. Visual elements are intentional; nothing is purely decorative. The system uses the logo's orbital motif as a metaphor for holistic oversight and focused intervention.

**Design Movements:**
- **Minimalism:** To emphasize clarity and focus on data/consulting insights.
- **Corporate Modern:** To maintain a professional, B2B relationship-driven atmosphere.
- **Tactile Clarity:** Using subtle shadows and defined borders to make "Diagnosis Cards" feel like tangible reports.

## Colors
The palette is built on a foundation of "Neutral Stability" and "Action Blue." 

- **Primary (#191f28):** A deep charcoal-navy used for primary typography, headers, and CTA backgrounds. It provides the weight of authority.
- **Secondary (#3182f6):** A vibrant, professional blue used sparingly for interactive elements, highlights, and status indicators. It signifies progress and digital precision.
- **Surface & Neutrals:** The background uses a soft off-white (#f9fafb) to reduce eye strain during long reading sessions. Pure white (#ffffff) is reserved for cards and modular content blocks to create a clear "layered" hierarchy.
- **Dimmed Text (#4e5968):** Used for secondary information and body text to create a comfortable reading contrast against the background.

## Typography
This design system utilizes **Plus Jakarta Sans** for headlines to provide a modern, slightly geometric feel that resonates with the logo's character. **Hanken Grotesk** is used for body copy and labels, chosen for its exceptional legibility and professional neutrality, especially in data-heavy consulting contexts.

For Korean implementation, pair these with **Pretendard JP/KR** as the system-level fall-back to ensure the character spacing and weight remain consistent across languages. 

**Usage Notes:**
- **Display LG:** Used for primary landing statements and hero sections.
- **Body MD:** The workhorse for reports and diagnosis descriptions; ensure a line-height of 1.6 to maintain readability.
- **Label SM:** Used for "Field Notes" and metadata, always in All Caps when in English to denote a "label" status.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy for desktop to maintain the "restrained" and "structured" feel of a consulting report. 

- **Desktop:** 12-column grid with a 1200px max-width. Large 120px vertical gaps between major service sections to emphasize the "Airy" and "Spacious" brand identity.
- **Tablet:** 8-column grid with 32px side margins.
- **Mobile:** 4-column fluid grid. Layouts should reflow vertically, with horizontal "Diagnosis Cards" transitioning to stacked vertical cards.

Spacing is based on a 4px baseline grid. Padding within cards and containers should be generous (typically 32px or 40px) to prevent the professional information from feeling cluttered.

## Elevation & Depth
Depth is used to separate "Strategy" from "Action." 

- **Low-Contrast Outlines:** The primary method for defining sections. Use 1px borders (#e5e8eb) for cards and accordions.
- **Ambient Shadows:** Reserved strictly for interactive "Diagnosis Cards" or hover states on CTA elements. Use a very soft, diffused shadow: `0px 4px 20px rgba(0, 0, 0, 0.04)`.
- **Tonal Layering:** The background (#f9fafb) acts as the base. White (#ffffff) surfaces sit on top, representing active "consulting modules."
- **Sticky Header:** Uses a Backdrop Blur (20px) with a semi-transparent white background (80% opacity) to maintain context while scrolling without creating a hard visual break.

## Shapes
The shape language is **Soft (0.25rem)**. 

Consulting requires a balance of "sharp" intellect and "soft" hospitality. While the layout is rigid and grid-based, the subtle rounding on buttons and cards prevents the UI from feeling overly clinical or aggressive. 

- **Standard Elements:** 4px (0.25rem) radius.
- **Large Cards:** 8px (0.5rem) radius.
- **Input Fields:** 4px (0.25rem) radius to maintain a formal, document-like feel.

## Components

### Sticky Header
- **Background:** Blur effect with white tint.
- **Content:** Logo on the left, utility navigation in the center, and a single "Get Diagnosis" CTA on the right in Primary Navy.
- **Height:** 72px fixed.

### AI Preliminary Diagnosis Cards
- **Style:** White surface, 1px border (#e5e8eb). 
- **Header:** Icon in Professional Blue (#3182f6) followed by a Title-LG.
- **Content:** Bulleted lists using the "Field-based" photography style as a background for one half of the card.

### Timeline Cards
- **Structure:** Vertical line in Border (#e5e8eb) with nodes in Primary Navy.
- **Content:** Left side shows the "Consulting Phase," right side shows "Specific Deliverables."

### Accordion FAQ
- **Visuals:** Flat style, separated by subtle borders. 
- **Interaction:** Smooth height expansion. Use a plus/minus toggle rather than a chevron to feel more "structural."

### Dark Navy CTA Sections
- **Background:** #191f28.
- **Typography:** All text in White (#ffffff).
- **Button:** Secondary Blue (#3182f6) with white text. This section should feel high-contrast and final, acting as the "Implementation" stage of the page.

### Imagery Integration
- **Field Photos:** Use high-resolution, unedited photos of hotel lobbies or maintenance areas. Apply a subtle desaturation or a cool-tone overlay to ensure they align with the Professional Navy palette.