import { Button } from "@/components/ui/button"
import { ArrowDown } from "lucide-react"

export const HomePage = () => {
  return (
    <section id="home" className="min-h-screen flex items-center justify-center bg-gradient-hero relative overflow-hidden">
      {/* Background Glow Effects */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-primary/10 rounded-full blur-3xl"></div>
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-accent/10 rounded-full blur-3xl"></div>
      
      <div className="container mx-auto px-6 text-center relative z-10">
        {/* Main Content */}
        <div className="max-w-4xl mx-auto">
          <h1 className="text-6xl md:text-8xl font-bold mb-6 bg-gradient-to-r from-foreground to-primary bg-clip-text text-transparent">
            Luis Martínez
          </h1> 
          
          
          <h2 className="text-xl md:text-2xl text-muted-foreground mb-8 max-w-3xl mx-auto leading-relaxed">
            Desarrollador Full-Stack
          </h2>
          <div className="mb-8">
            <p className="text-muted-foreground mb-6">
              Crea experiencias digitales de alto rendimiento, integrando diseño innovador con funcionalidad robusta.
            </p>
          </div>
          {/* Status Indicator */}
          <div className="flex items-center justify-center gap-3 mb-8">
            <div className="w-3 h-3 bg-accent rounded-full animate-pulse"></div>
            <span className="text-accent font-medium">Disponible para nuevos proyectos</span>
          </div>

          {/* CTA Button */}
          <Button 
            variant="ghost" 
            size="lg"
            
            className="group"
          >
            Ve mis proyectos
            <ArrowDown className="ml-2 group-hover:translate-y-1 transition-transform" />
          </Button>
        </div>

        {/* Technology Stack */}
        {/* <div className="mt-16">
          <TechStack />
        </div> */}
      </div>
    </section>
  )
}
