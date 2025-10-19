import { Button } from "@/components/ui/button"
import { Outlet } from "react-router"
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet";
import { Menu } from "lucide-react";

export const PorfolioLayout = () => {
  
  return (
    <div className="min-h-screen bg-background">
      <header className="fixed top-0 left-0 right-0 z-50 bg-background/80 backdrop-blur-md border-b border-border">
        <div className="container mx-auto px-6 py-4">
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

            <div className="hidden md:flex items-center w-full">
              {/* Navigation Links */}
              <div className="mx-auto flex items-center space-x-8">
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
                {/* CTA Button */}
                
              </div>
              <Button 
                variant="hero" 
                size="sm"
                // onClick={}
              >
                Contacto
              </Button>
            </div>
            
            <div className="block md:hidden">
            <Sheet>
              <SheetTrigger asChild>
                <Button variant="outline" size="sm">
                  <Menu className="h-4 w-4" />
                </Button>
              </SheetTrigger>
              <SheetContent side="right" className="w-[300px] sm:w-[400px]">
                <div className="flex flex-col space-y-4 mt-8">
                  <Button 
                    variant="nav" 
                    size="lg" 
                    // onClick={() => scrollToSection('home')}
                    className="justify-start"
                  >
                    Home
                  </Button>
                  <Button 
                    variant="nav" 
                    size="lg" 
                    // onClick={() => scrollToSection('services')}
                    className="justify-start"
                  >
                    Servicios
                  </Button>
                  <Button 
                    variant="nav" 
                    size="lg" 
                    // onClick={() => scrollToSection('projects')}
                    className="justify-start"
                  >
                    Proyectos
                  </Button>
                  <Button 
                    variant="nav" 
                    size="lg" 
                    // onClick={() => scrollToSection('contact')}
                    className="justify-start"
                  >
                    Conoceme
                  </Button>
                  <Button 
                    variant="hero" 
                    size="lg"
                    // onClick={() => scrollToSection('contact')}
                    className="mt-4"
                  >
                    Contacto
                  </Button>
                </div>
              </SheetContent>
            </Sheet>
          </div>

          </nav>
          

        </div>
      </header>
      <Outlet/>
    </div>
  )
}
