import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Message } from 'src/app/models/ia/Message';
import { IaService } from 'src/app/services/ia.service';

@Component({
  selector: 'app-interfaces-ui',
  templateUrl: './interfaces-ui.component.html',
  styleUrls: ['./interfaces-ui.component.scss']
})
export class InterfacesUiComponent implements OnInit {

  // Variables globales
  interfacesListMessage: any = []; 
  interfacesForm: FormGroup;
  respuesta: string = "";
  
  constructor(
    private formBuilder: FormBuilder,
    private iaService: IaService
    ) { 
      this.interfacesForm = this.formBuilder.group({
        message: ['', [Validators.required]],
        response: ['']
      })
  }

  ngOnInit(): void {
  }

  private loadForm(){
    
    this.interfacesForm.patchValue({
      response: this.respuesta
    })
  }

 public onSubmit(){
    let message : Message = this.interfacesForm.value; 
    
    this.iaService.sendMessage(message).subscribe( date => {

      let respuestaObtenida = JSON.stringify(date)
      let respuestaFiltrada = JSON.parse(respuestaObtenida)

      this.respuesta = respuestaFiltrada.response
      this.respuesta.replace(/\n/g, "");
      
      this.loadForm()
    })
  }
}
