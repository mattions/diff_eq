@model:2.1.0=model_0000001 "dAlcantara2003_SynapticPlasticity"
@units
 substance=mole:s=-6 "substance"
@compartments
 compartment_0000001=1.0 "spine"
@species
 compartment_0000001:[Sstar]=0.0b "S*"
 compartment_0000001:[K]=0.5 "K"
 compartment_0000001:[Kprime]=0.0 "K'"
 compartment_0000001:[Kstar]=0.0 "K*"
 compartment_0000001:[N]=1.0 "N"
 compartment_0000001:[Nstar]=0.0 "N*"
 compartment_0000001:[D]=3.0 "D"
 compartment_0000001:[Dstar]=0.0 "D*"
 compartment_0000001:[R]=1.0 "R"
 compartment_0000001:[Rprime]=0.0 "R'"
 compartment_0000001:[Rstar]=0.0 "R*"
 compartment_0000001:[Pstar]=2.0 "P*"
 compartment_0000001:[DstarP]=0.0 "D*P"
 compartment_0000001:[Stotal]=30.0c "S total"
 compartment_0000001:[Ca2plus]=0.001 "Ca2plus"
@parameters
 Kd=7.0 "Kd"
 nH=4.0 "Hill coefficient"
 k1=150.0 "k1"
 k2=2.17 "k2"
 k3=0.5 "k3"
 k4=0.03 "k4"
 n1=1666.0 "n1"
 n2=10.0 "n2"
 d1=2000.0 "d1"
 d2PKAstar=0.002 "d2 times PKA*"
 r1PKAstar=0.1 "r1 times PKA*"
 r2=1.0 "r2"
 r3=10.0 "r3"
 r4=0.1 "r4"
 p1=0.03 "p1"
 p2=3e-05 "p2"
@rules
 Ca2plus = piecewise(0.1, lt(time, 60), 0.1, gt(time, 66.0115), 1)
 Sstar = (Stotal - (Kprime + Kstar + Nstar)) / (1 + pow(Kd / Ca2plus, nH))
@reactions
@r=reaction_0000003 "CaMKII binding to CaM"
 K+Sstar -> Kprime
 k1 * Sstar * K * compartment_0000001
@r=reaction_0000004 "CaMKII autophosphorylation"
 Kprime -> Kstar
 k3 * Kprime * compartment_0000001
@r=reaction_0000006 "Calcineurin or PP2B activation"
 N+Sstar -> Nstar
 n1 * Sstar * N * compartment_0000001
@r=reaction_0000007 "DARPP-32 activation"
 D -> Dstar
 d2PKAstar * D * compartment_0000001
@r=reaction_0000008 "AMPAR intermediate activation"
 R -> Rprime
 r1PKAstar * R * compartment_0000001
@r=reaction_0000009 "full AMPAR activation by active CaMKII"
 Rprime -> Rstar : Kprime
 r3 * Rprime * Kprime * compartment_0000001
@r=reaction_0000010 "PP1 inactivation"
 Dstar+Pstar -> DstarP
 p2 * Dstar * Pstar * compartment_0000001
@r=reaction_0000011 "CaM unbinding from CaMKII"
 Kprime -> K+Sstar
 k2 * Kprime * compartment_0000001
@r=reaction_0000012 "CaMKII dephosphorylation"
 Kstar -> Kprime : Pstar
 Kstar * k4 * Pstar * compartment_0000001
@r=reaction_0000014 "Calcineurin or PP2B inactivation"
 Nstar -> Sstar+N
 Nstar * n2 * compartment_0000001
@r=reaction_0000015 "DARPP-32 deactivation"
 Dstar -> D : Nstar
 Dstar * Nstar * d1 * compartment_0000001
@r=reaction_0000016 "AMPAR complete deactivation by calcineurin"
 Rprime -> R : Nstar
 Rprime * r2 * Nstar * compartment_0000001
@r=reaction_0000017 "AMPAR complete deactivation by PP1"
 Rprime -> R : Pstar
 Rprime * r2 * Pstar * compartment_0000001
@r=reaction_0000019 "full AMPAR activation by autophosphorylated CaMKII"
 Rprime -> Rstar : Kstar
 Rprime * r3 * Kstar * compartment_0000001
@r=reaction_0000020 "intermediate AMPAR deactivation"
 Rstar -> Rprime : Pstar
 Rstar * r4 * Pstar * compartment_0000001
@r=reaction_0000021 "PP1 activation"
 DstarP -> Dstar+Pstar
 DstarP * p1 * compartment_0000001
