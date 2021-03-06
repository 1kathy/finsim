/*FinSim
Copyright 2018 Carnegie Mellon University. All Rights Reserved.
NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
Released under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.
*/

import { Component, OnInit } from '@angular/core';
import { BankAccount } from '../bank-account';
import { FinSimService } from '../fin-sim.service';

@Component
({
  selector: 'app-accounts',
  templateUrl: './accounts.component.html',
  styleUrls: ['./accounts.component.css']
})
export class AccountsComponent implements OnInit
{
  accounts: BankAccount[];

  constructor( private finSimService: FinSimService ) { }

  ngOnInit()
  {
    var service = this;
    this.finSimService.getAccounts().subscribe
    ({
      next( accounts )
      {
        service.accounts = accounts;
      },
      error( msg )
      {
        console.log( msg );
      }
    });
  }

}
