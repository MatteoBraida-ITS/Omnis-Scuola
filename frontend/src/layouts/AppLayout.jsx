import AppSidebar from "@/components/AppSidebar";
import { SidebarProvider } from "@/components/ui/sidebar";

function AppLayout() {
  return (
    <SidebarProvider>
      <AppSidebar ruolo="docente"></AppSidebar>
      <header></header>
      <main>Dashboard</main>
    </SidebarProvider>
  );
}
export default AppLayout;
