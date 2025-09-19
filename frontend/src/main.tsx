import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import { WebCloudForgeApp } from './WebCloudForgeApp'


createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <WebCloudForgeApp/>
  </StrictMode>,
)
