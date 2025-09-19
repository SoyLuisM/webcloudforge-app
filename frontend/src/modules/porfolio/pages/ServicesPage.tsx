import { Card } from "@/components/ui/card";
import { ChartColumnStacked, Code, Database, Server } from "lucide-react";


const services = [
    {
        icon: Code,
        title: "Desarrollo Frontend",
        description: "Aplicaciones web modernas y responsivas construidas con React, TypeScript y tecnologías de vanguardia.",
        skills: ["React", "TypeScript", "Tailwind CSS"]
    },
    {
        icon: Server,
        title: "Desarrollo Backend", 
        description: "Soluciones escalables del lado del servidor con APIs robustas, autenticación e infraestructura en la nube.",
        skills: ["Node.js", "Python", "REST APIs","Microservicios"]
    },
    {
        icon: Database,
        title: "Gestión de Datos",
        description: "Diseño de bases de datos eficiente, optimización y procesamiento de datos para aplicaciones complejas.",
        skills: ["PostgreSQL", "MongoDB", "Redis"]
    },
    {
        icon: ChartColumnStacked ,
        title: "Analisis de datos",
        description: "Conversión de datos complejos en insights accionables para impulsar la toma de decisiones estratégicas del negocio.",
        skills: ["PostgreSQL", "Pyton", "ETL Pipelines", "Scipy", "Tensorflow"]
    },
    
];

export const ServicesPage = () => {
  return (
    <section id="services" className="py-20 px-6">
      <div className="container mx-auto max-w-6xl">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-6">¿Como puedo ayudarte?</h2>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            Me especializo en crear soluciones digitales de extremo a extremo que combinan un diseño atractivo 
            con una funcionalidad poderosa para ayudar a las empresas a alcanzar sus objetivos.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {services.map((service) => (
            <Card 
              key={service.title}
              className="p-8 bg-gradient-card border-border hover:border-primary/50 transition-all duration-300 hover:shadow-card group cursor-pointer"
            >
              <div className="mb-6">
                <div className="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center mb-4 group-hover:bg-primary/20 transition-colors">
                  <service.icon className="w-6 h-6 text-primary" />
                </div>
                <h3 className="text-xl font-semibold mb-3">{service.title}</h3>
                <p className="text-muted-foreground leading-relaxed mb-4">
                  {service.description}
                </p>
              </div>
              
              <div className="flex flex-wrap gap-2">
                {service.skills.map((skill) => (
                  <span 
                    key={skill}
                    className="px-3 py-1 text-xs bg-secondary text-secondary-foreground rounded-full"
                  >
                    {skill}
                  </span>
                ))}
              </div>
            </Card>
          ))}
        </div>
      </div>
    </section>
  )
}
