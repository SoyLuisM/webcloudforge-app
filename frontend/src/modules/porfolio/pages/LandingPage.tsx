import { AboutPage } from "./AboutPage"
import { ContactPage } from "./ContactPage"
import { FooterPage } from "./FooterPage"
import { HomePage } from "./HomePage"
import { ProjectsApp } from "./ProjectsApp"
import { ServicesPage } from "./ServicesPage"


export const LandingPage = () => {
  return (
    <>
        <HomePage/>
        <ServicesPage/>
        <ProjectsApp/>
        <AboutPage/>
        <ContactPage/>
        <FooterPage/>
    </>
  )
}
