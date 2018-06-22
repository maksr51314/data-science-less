
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
class E(B): pass
class F(C): pass
class G(D, E): pass
class H(G, F): pass
