import { sidebarItems } from "@/config/sidebarItems";
import {
  Sidebar,
  SidebarContent,
  SidebarGroup,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "./ui/sidebar";

function AppSidebar({ ruolo }) {
  const vociVisibili = sidebarItems.filter((item) =>
    item.ruoli.includes(ruolo),
  );
  return (
    <Sidebar>
      <SidebarContent>
        <SidebarGroup>
          <SidebarMenu>
            {vociVisibili.map((voce) => (
              <SidebarMenuItem key={voce.titolo}>
                <SidebarMenuButton render={<a href={voce.url}></a>}>
                  <voce.icona />
                  {voce.titolo}
                </SidebarMenuButton>
              </SidebarMenuItem>
            ))}
          </SidebarMenu>
        </SidebarGroup>
      </SidebarContent>
    </Sidebar>
  );
}
export default AppSidebar;
