import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"
import { ExternalLink, Github } from "lucide-react"


const projects = [
    {
      title: "Plataforma webcloudforge.com",
      description:
        "Un proyecto full-stack forjado para ofrecer una solución de portafolio personal que es rápida, eficiente y de bajo costo. Combina una landing page estática de alto rendimiento con un panel de administración para un control total sobre el contenido.",
      image: "/modern-ecommerce-dashboard.png",
      technologies: ["React", "Python", "PostgreSQL", "Fastapi", "Cloudflare"],
      githubUrl: "https://github.com",
      liveUrl: "https://example.com",
      
    },
    {
      title: "Solución de Inteligencia de Negocio para la Gestión Académica",
      description:
        "Desarrollo de un pipeline de datos (ELT) que automatiza la extracción y transformación de la información académica. El sistema centraliza los indicadores clave (KPIs) para facilitar la toma de decisiones estratégicas y optimizar la gestión universitaria.",
      image: "/task-management-app-interface-dark-theme.jpg",
      technologies: ["Python", "Scipy", "Tensorflow"],
      githubUrl: "https://github.com",
      liveUrl: "https://example.com",
      
    },
    {
      title: "Dashboard empresarial",
      description:
        "Desarrollo de una solución integral de inteligencia de negocio para el monitoreo de indicadores clave. La plataforma transforma datos complejos de una base de datos PostgreSQL en visualizaciones interactivas mediante un frontend en React y una API RESTful de alto rendimiento construida con FastAPI, facilitando la toma de decisiones estratégicas basadas en datos.",
      image: "/ai-content-generator-interface-modern-design.jpg",
      technologies: ["Python", "FastAPI", "React", "Docker"],
      githubUrl: "https://github.com",
      liveUrl: "https://example.com",
      
    },
]

export const ProjectsApp = () => {
  return (
    <section id="projects" className="py-20 px-6">
      <div className="container mx-auto max-w-6xl">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-6">Conoce mis proyectos</h2>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            Estos son algunos de mis proyectos recientes que demuestran mis habilidades en desarrollo full-stack, 
            manejo de servidores y visualización de datos.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-8">
          {projects.map((project) => (
            <Card 
              key={project.title}
              className="overflow-hidden bg-gradient-card border-border hover:border-primary/50 transition-all duration-300 hover:shadow-card group"
            >
              {/* Project Image */}
              <div className="relative overflow-hidden">
                <img 
                  src='/placeholder.svg'
                  alt={project.title}
                  className="w-full h-48 object-cover group-hover:scale-105 transition-transform duration-300"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-card/80 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
              </div>

              {/* Project Content */}
              <div className="p-6">
                <h3 className="text-xl font-semibold mb-3">{project.title}</h3>
                <p className="text-muted-foreground text-sm leading-relaxed mb-4">
                  {project.description}
                </p>

                {/* Technologies */}
                <div className="flex flex-wrap gap-2 mb-6">
                  {project.technologies.map((tech) => (
                    <span 
                      key={tech}
                      className="px-2 py-1 text-xs bg-secondary text-secondary-foreground rounded-md"
                    >
                      {tech}
                    </span>
                  ))}
                </div>

                {/* Action Buttons */}
                <div className="flex gap-3">
                  <Button variant="outline" size="sm" asChild>
                    <a href={project.githubUrl} target="_blank" rel="noopener noreferrer">
                      <Github className="w-4 h-4 mr-2" />
                      GitHub
                    </a>
                  </Button>
                  <Button variant="default" size="sm" asChild>
                    <a href={project.liveUrl} target="_blank" rel="noopener noreferrer">
                      <ExternalLink className="w-4 h-4 mr-2" />
                      Live Demo
                    </a>
                  </Button>
                </div>
              </div>
            </Card>
          ))}
        </div>
      </div>
    </section>
  )
}
