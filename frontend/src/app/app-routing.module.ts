import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InterfacesUiComponent } from './pages/interfaces-ui/interfaces-ui.component';

const routes: Routes = [
  {
    path:"**",
    redirectTo:"interfacesUi",
    pathMatch: "full"
  },
  {
    path:"interfacesUi",
    component: InterfacesUiComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
