import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-lg text-sm font-medium ring-offset-background transition-all duration-300 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0",
  {
    variants: {
      variant: {
        // default:
        //   "bg-primary text-primary-foreground shadow-xs hover:bg-primary/90",
        // destructive:
        //   "bg-destructive text-white shadow-xs hover:bg-destructive/90 focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40 dark:bg-destructive/60",
        // outline:
        //   "border bg-background shadow-xs hover:bg-accent hover:text-accent-foreground dark:bg-input/30 dark:border-input dark:hover:bg-input/50",
        // secondary:
        //   "bg-secondary text-secondary-foreground shadow-xs hover:bg-secondary/80",
        // ghost:
        //   "hover:bg-accent hover:text-accent-foreground dark:hover:bg-accent/50",
        // link: "text-primary underline-offset-4 hover:underline",
        // hero: "bg-gradient-accent text-primary-foreground hover:shadow-glow transform hover:scale-105 font-semibold",
        // nav: "text-foreground hover:text-primary transition-colors",
        default: "bg-primary text-primary-foreground hover:bg-primary/90 shadow-lg hover:shadow-glow transform hover:scale-105",
        destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
        outline: "border border-border bg-background/50 backdrop-blur-sm hover:bg-card hover:border-primary/50 text-foreground",
        secondary: "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        ghost: "hover:bg-accent/20 hover:text-accent-foreground text-muted-foreground",
        link: "text-primary underline-offset-4 hover:underline",
        hero: "btn-hero",
        nav: "text-foreground hover:text-primary transition-colors",
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 rounded-md px-3",
        lg: "h-11 rounded-md px-8",
        icon: "h-10 w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

function Button({
  className,
  variant,
  size,
  asChild = false,
  ...props
}: React.ComponentProps<"button"> &
  VariantProps<typeof buttonVariants> & {
    asChild?: boolean
  }) {
  const Comp = asChild ? Slot : "button"

  return (
    <Comp
      data-slot="button"
      className={cn(buttonVariants({ variant, size, className }))}
      {...props}
    />
  )
}

export { Button, buttonVariants }
