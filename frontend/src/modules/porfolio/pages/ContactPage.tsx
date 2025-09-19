import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card'
import { Mail,Linkedin, Github } from 'lucide-react'


const socialLinks = [
    {
      name: "LinkedIn",
      icon: Linkedin,
      url: "https://linkedin.com/in/jorge-l-martinez-hernandez",
      color: "hover:text-blue-400"
    },
    {
      name: "GitHub", 
      icon: Github,
      url: "https://github.com/SoyLuisM",
      color: "hover:text-gray-400"
    },
  ];

export const ContactPage = () => {
  return (
    <section id="contact" className="py-20 px-6">
      <div className="container mx-auto max-w-4xl">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-6">Trabajemos juntos</h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto leading-relaxed">
            ¿Tienes una idea o una oportunidad laboral? Me encantaría conocerla.
          </p>
        </div>

        <Card className="p-8 md:p-12 bg-gradient-card border-border text-center">
          <div className="space-y-8">
            {/* Email */}
            <div className="space-y-4">
              <div className="flex items-center justify-center gap-3">
                <Mail className="w-6 h-6 text-primary" />
                <span className="text-lg font-medium">Enviame un Email</span>
              </div>
              <a 
                href="mailto:luismartinezh@webcloudforge.com"
                className="text-2xl md:text-3xl font-semibold text-primary hover:text-primary/80 transition-colors"
              >
                luismartinezh@webcloudforge.com
              </a>
            </div>

            {/* Divider */}
            <div className="relative">
              <div className="absolute inset-0 flex items-center">
                <div className="w-full border-t border-border"></div>
              </div>
              <div className="relative flex justify-center text-sm">
                <span className="bg-card px-4 text-muted-foreground">o encuentrame en</span>
              </div>
            </div>

            {/* Social Links */}
            <div className="flex items-center justify-center gap-6">
              {socialLinks.map((social) => (
                <Button
                  key={social.name}
                  variant="outline"
                  size="lg"
                  asChild
                  className="group"
                >
                  <a 
                    href={social.url} 
                    target="_blank" 
                    rel="noopener noreferrer"
                    className="flex items-center gap-3"
                  >
                    <social.icon className={`w-5 h-5 transition-colors ${social.color}`} />
                    {social.name}
                  </a>
                </Button>
              ))}
            </div>

            {/* CTA */}
            <div className="pt-4">
              <Button className="bg-accent hover:bg-accent/90 text-accent-foreground" size="lg" asChild>
                <a href="mailto:luismartinezh@webcloudforge.com">
                  Iniciar conversacion
                </a>
              </Button>
            </div>
          </div>
        </Card>

        
      </div>
    </section>
  )
}
