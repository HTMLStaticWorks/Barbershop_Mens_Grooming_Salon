---
name: Midnight Chrome & Crimson
colors:
  surface: '#141313'
  surface-dim: '#141313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2b2a2a'
  surface-container-highest: '#353434'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#111111'
  on-primary-container: '#7e7c7c'
  inverse-primary: '#5f5e5e'
  secondary: '#e6c364'
  on-secondary: '#3d2e00'
  secondary-container: '#785d00'
  on-secondary-container: '#fdd977'
  tertiary: '#ffb4a9'
  on-tertiary: '#690001'
  tertiary-container: '#2d0000'
  on-tertiary-container: '#da4c3b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#ffe08f'
  secondary-fixed-dim: '#e6c364'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#584400'
  tertiary-fixed: '#ffdad5'
  tertiary-fixed-dim: '#ffb4a9'
  on-tertiary-fixed: '#410000'
  on-tertiary-fixed-variant: '#8e130c'
  background: '#141313'
  on-background: '#e5e2e1'
  surface-variant: '#353434'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '800'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
  button:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  header_height: 72px
  container_max_width: 1200px
  gutter: 24px
  margin_mobile: 16px
  stack_sm: 8px
  stack_md: 16px
  stack_lg: 32px
  section_padding: 80px
---

## Brand & Style
The design system embodies a premium, urban barbershop aesthetic that balances old-world craftsmanship with modern luxury. The target audience is the discerning man who values precision, tradition, and a high-end service environment.

The style is **Dark Luxury**—a mix of high-contrast minimalism and tactile elegance. It utilizes heavy blacks, metallic gold highlights, and sharp, intentional layouts to evoke a sense of exclusivity. The interface should feel as sharp as a straight razor: precise, weighted, and sophisticated.

Key stylistic markers include:
- High contrast between deep backgrounds and metallic accents.
- Sophisticated use of whitespace to frame content like editorial photography.
- Subtle glassmorphism on navigation elements to maintain a modern, technical edge.

## Colors
This design system uses a palette rooted in **Midnight Black** to establish authority and depth. **Gold Chrome** is reserved for primary actions, branding, and status indicators, mimicking the brass and gold hardware of a luxury shop. **Crimson Red** serves as a high-energy accent for urgent notifications or specific "Book Now" highlights.

In **Light Mode**, the palette shifts to a warm "parchment" feel (`#F7F4F0`) to maintain a classic, editorial look without the harshness of pure white. In **Dark Mode**, the surfaces are deep and layered to reduce eye strain while making the gold accents pop with a "glow" effect.

## Typography
The typographic hierarchy creates a tension between the traditional elegance of **Playfair Display** and the functional precision of **Inter**.

- **Headlines:** Use Playfair Display with tight tracking for a bold, editorial feel. Large display sizes should use the 800 weight for maximum impact on hero sections.
- **Body:** Inter provides maximum legibility for service menus and descriptions. Use the 500 weight for lead paragraphs to maintain a "heavy" premium feel.
- **Labels:** Small caps and increased letter spacing are used for "overlines" and technical details to mimic high-end product packaging.

## Layout & Spacing
The layout follows a **Fixed Grid** model on desktop (1200px max-width) to create a curated, centered viewing experience. 

- **Grid:** 12-columns with a 24px gutter.
- **Header:** A fixed 72px height. It must include a `backdrop-blur(12px)` effect with a 70% opacity background color (Midnight Black in dark mode, Parchment in light mode) to maintain legibility during scroll.
- **Section Spacing:** Generous vertical padding (80px+) is required between major content blocks to emphasize the "Minimalist Luxury" aesthetic and prevent visual clutter.
- **Mobile:** Transition to a 4-column fluid grid with 16px side margins.

## Elevation & Depth
Depth is achieved through **Tonal Layering** and **Selective Accents** rather than heavy shadows.

- **Level 0 (Base):** The primary background color.
- **Level 1 (Cards):** Surfaces should have a subtle 1px border. In dark mode, use a 2px top-border in Gold Chrome (#C9A84C) to signify interactive or featured content.
- **Shadows:** Avoid large, fuzzy shadows. If depth is required, use a sharp "cut-out" shadow: `0px 4px 0px 0px rgba(0,0,0,0.2)` to maintain a masculine, architectural feel.
- **Glassmorphism:** Reserved exclusively for the sticky header and dropdown menus to provide a sense of modern technology overlaying traditional textures.

## Shapes
The design utilizes "Precise Geometry." While the brand is sharp, a standard radius of **12px** (rounded-lg) is applied to all cards and primary containers to soften the "Brutalist" edges just enough for a premium UI feel.

- **Buttons:** 4px radius (Soft) for a more technical, tool-like appearance.
- **Inputs:** 8px radius.
- **Cards:** 12px radius.
- **Media/Images:** Always sharp (0px) or very slightly rounded (4px) to mimic framed photography.

## Components
- **Primary Buttons:** High-contrast Gold Chrome (#C9A84C) background with Midnight Black text. Heavy weight, uppercase typography.
- **Secondary Buttons:** Ghost style with a 1px Midnight Black (or Light Text) border and no fill.
- **Cards:** Use the defined `surface` color with a 1px `border` color. For "Featured Services," add a 2px Gold Chrome top border.
- **Input Fields:** Bottom-border only (minimalist style) or full 1px stroke. Focus state should highlight the border in Gold Chrome.
- **Chips/Badges:** Small, rectangular with 2px radius. Use Crimson Red for "New" or "Hot" status items to draw immediate attention.
- **Lists:** Service items should be separated by a subtle 1px horizontal line, with prices set in Playfair Display (700 weight) for an artisanal feel.
- **Booking Widget:** Should be anchored or highly visible, using the Crimson Red accent sparingly for the final "Confirm" action to differentiate from browsing.