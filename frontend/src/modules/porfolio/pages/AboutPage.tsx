import { Card } from "@/components/ui/card";

const experience = [
    {
      title: "Desarrollador independiente Full-Stack ",
      company: "Independiente",
      period: "2025 - Actualmente",
      description:
        "Construccion de arquitecturas y proyectos de bajo costo y alto rendimiento a la vez que asesoro estudiantes universitarios, guiándolos para que superen las mismas barreras que yo he enfrentado.",
    },
    {
      title: "Desarrollador web",
      company: "Corporación Disruptiva Itzamná",
      period: "2023 - 2025",
      description:
        "Fui responsable del diseño, construcción y mantenimiento de soluciones web empresariales, principalmente de sistemas backend escalables utilizando Django REST Framework y administré bases de datos PostgreSQL y MongoDB para garantizar la integridad y el rendimiento en producción.",
    },
    {
      title: "Junior Developer",
      company: "Soporti",
      period: "2020 - 2021",
      description:
        "Desarrollé y mantuve sitios web de clientes utilizando frameworks JavaScript modernos. Adquirí experiencia en todo el ciclo de desarrollo.",
    },
  ]

  const education = [
    {
      title: "Ingeniería en Telemática",
      institution: "Unidad Profesional Interdisciplinaria en Ingeniería y tecnologías Avanzadas-IPN",
      period: "2018 - 2025",
      description: "Mi enfoque academico se centró en el desarrollo web y ciencia de datos"
    },
    
  ]
export const AboutPage = () => {
  return (
    <section id="footer" className="py-20 px-6">
      <div className="container mx-auto max-w-6xl">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-6">Acerca de mí</h2>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-12 items-start">
          {/* Photo and Bio */}
          <div className="lg:col-span-1">
            <div className="text-center lg:text-left">
              {/* <div className="relative inline-block mb-6">
                <img 
                  src=""
                  alt="Luis Martinez"
                  className="w-48 h-48 rounded-2xl object-cover shadow-card border border-border"
                />
                <div className="absolute inset-0 rounded-2xl bg-gradient-accent opacity-10"></div>
              </div> */}
              
              <div className="space-y-4">
                <p className="text-muted-foreground leading-relaxed">
                    Mi viaje en la tecnología comenzó con una fascinación por resolver problemas complejos, 
                    pero ha encontrado su verdadero propósito en resolver problemas humanos. 
                    Como desarrollador de software, mi pasión es forjar herramientas que sean no solo eficientes y escalables, 
                    sino fundamentalmente accesibles.
                </p>
                <p className="text-muted-foreground leading-relaxed">
                    Esta misión la aplico en dos frentes: técnicamente, construyendo arquitecturas de bajo costo y alto rendimiento 
                    como la que impulsa a WebCloudForge; y humanamente, como asesor de estudiantes universitarios, 
                    guiándolos para que superen las mismas barreras que yo he enfrentado.
                </p>
                
              </div>
            </div>
          </div>

          {/* Experience and Education */}
          <div className="lg:col-span-2 grid grid-cols-1 md:grid-cols-2 gap-8">
            {/* Professional Experience */}
            <div>
              <h3 className="text-2xl font-semibold mb-6 text-center md:text-left">Experiencia Profesional</h3>
              <div className="space-y-6">
                {experience.map((job, index) => (
                  <Card key={index} className="p-6 bg-gradient-card border-border">
                    <div className="space-y-2">
                      <h4 className="font-semibold text-foreground">{job.title}</h4>
                      <p className="text-primary font-medium">{job.company}</p>
                      <p className="text-sm text-muted-foreground">{job.period}</p>
                      <p className="text-sm text-muted-foreground leading-relaxed">{job.description}</p>
                    </div>
                  </Card>
                ))}
              </div>
            </div>

            {/* Education */}
            <div>
              <h3 className="text-2xl font-semibold mb-6 text-center md:text-left">Educación</h3>
              <div className="space-y-6">
                {education.map((edu, index) => (
                  <Card key={index} className="p-6 bg-gradient-card border-border">
                    <div className="space-y-2">
                      <h4 className="font-semibold text-foreground">{edu.title}</h4>
                      <p className="text-primary font-medium">{edu.institution}</p>
                      <p className="text-sm text-muted-foreground">{edu.period}</p>
                      <p className="text-sm text-muted-foreground leading-relaxed">{edu.description}</p>
                    </div>
                  </Card>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
