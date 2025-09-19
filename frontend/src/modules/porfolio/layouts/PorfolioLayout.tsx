import { Button } from "@/components/ui/button"
import { Outlet } from "react-router"


export const PorfolioLayout = () => {
  return (
    <div className="min-h-screen bg-background">
      <header className="fixed top-0 left-0 right-0 z-50 bg-background/80 backdrop-blur-md border-b border-border">
        <div className="container mx-auto px-6 py-2">
          <nav className="flex items-center justify-between">
            {/* Logo/Name */}
            {/* <div className="text-xl font-bold text-foreground">
              Luis Martinez
            </div> */}
            <img 
              src='favicon/web-app-manifest-192x192.png'
              alt="Luis Martinez"
              className="h-15 object-cover group-hover:scale-105 transition-transform duration-300"
            />

            {/* Navigation Links */}
            <div className="hidden md:flex items-center space-x-8">
              <Button 
                variant="nav" 
                size="sm" 
                // onClick={}
              >
                Home
              </Button>
              <Button 
                variant="nav" 
                size="sm" 
                // onClick={}
              >
                Servicios
              </Button>
              <Button 
                variant="nav" 
                size="sm" 
                // onClick={}
              >
                Proyectos
              </Button>
              <Button 
                variant="nav" 
                size="sm" 
                // onClick={}
              >
                Conóceme
              </Button>
            </div>

            {/* CTA Button */}
            <Button 
              variant="hero" 
              size="sm"
              // onClick={}
            >
              Contacto
            </Button>
          </nav>
        </div>
      </header>
      <Outlet/>
    </div>
  )
}
