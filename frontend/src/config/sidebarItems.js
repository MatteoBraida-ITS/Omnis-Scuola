import { BookCheck } from "lucide-react";
import { FolderOpen } from "lucide-react";
import { LayoutDashboard } from "lucide-react";
import { Calendar1 } from "lucide-react";
import { ChartBellCurve } from "lucide-react";
import { GraduationCap } from "lucide-react";

export const sidebarItems = [
  {
    titolo: "Dashboard",
    url: "/dashboard",
    icona: LayoutDashboard,
    ruoli: ["docente", "studente", "segreteria"],
  },
  {
    titolo: "Classi",
    url: "/classi",
    icona: GraduationCap,
    ruoli: ["docente", "segreteria"],
  },
  {
    titolo: "Verifiche",
    url: "/verifiche",
    icona: BookCheck,
    ruoli: ["docente", "studente"],
  },
  {
    titolo: "Voti",
    url: "/voti",
    icona: ChartBellCurve,
    ruoli: ["docente", "studente"],
  },
  {
    titolo: "Materiale",
    url: "/materiale",
    icona: FolderOpen,
    ruoli: ["docente", "studente"],
  },
  {
    titolo: "Calendario",
    url: "/calendario",
    icona: Calendar1,
    ruoli: ["docente", "studente"],
  },
];
