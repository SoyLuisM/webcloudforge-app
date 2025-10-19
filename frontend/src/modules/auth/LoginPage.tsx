import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"


export const LoginPage = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-background p-4">
      <Card className="w-full max-w-md bg-project-card p-8 border-border/50">
        <div className="text-center mb-8">
          <h1 className="text-2xl font-bold text-foreground mb-2">Login</h1>
          <p className="text-muted-foreground">Accede al panel de control</p>
        </div>

        <form  className="space-y-6">
          <div className="space-y-2">
            <Label htmlFor="email" className="text-foreground">Email</Label>
            <Input
              id="email"
              type="email"
            //   value={email}
            //   onChange={(e) => setEmail(e.target.value)}
              placeholder="admin@example.com"
              className="bg-input border-border text-foreground"
              required
            />
          </div>

          <div className="space-y-2">
            <Label htmlFor="password" className="text-foreground">Contraseña</Label>
            <Input
              id="password"
              type="password"
            //   value={password}
            //   onChange={(e) => setPassword(e.target.value)}
              placeholder="••••••••"
              className="bg-input border-border text-foreground"
              required
            />
          </div>

          <Button 
            type="submit" 
            className="w-full"
            variant="hero"
          >
            Login 
          </Button>
        </form>

        <div className="mt-6 pt-6 border-t border-border">
          <Button 
            variant="ghost" 
            // onClick={() => navigate("/")}
            className="w-full text-muted-foreground hover:text-foreground"
          >
            ← Volver al portafolio
          </Button>
        </div>
      </Card>
    </div>
  )
}
