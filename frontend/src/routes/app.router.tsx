import { LoginPage } from "@/modules/auth/LoginPage";
import { ErrorPage } from "@/modules/errors/ErrorPage";
import { PorfolioLayout } from "@/modules/porfolio/layouts/PorfolioLayout";
import { LandingPage } from "@/modules/porfolio/pages/LandingPage";
import { createBrowserRouter } from "react-router";


export const appRouter = createBrowserRouter([
  {
    path: "/",
    element: <PorfolioLayout/>,
    children:[
        {
            index: true,
            element: <LandingPage/>
        },
        {
            path: '*',
            element: <ErrorPage/>
        },
    ]
  },
  {
    path: "login",
    element: <LoginPage/>
  }
])