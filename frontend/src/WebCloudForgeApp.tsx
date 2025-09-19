import { RouterProvider } from "react-router/dom"
import { appRouter } from "./routes/app.router"


export const WebCloudForgeApp = () => {
    
  return (
    <RouterProvider router={appRouter} />
  )
}
