mu=10.0
sigma2 = 4.0
nu = 12.0
r2 = 4


def m_update(mu,sigma2,nu,r2):
    sigma2_p = 1.0/((1.0/sigma2)+(1.0/r2))
    mu_p = ((r2*mu)+(sigma2*nu)) / (r2 + sigma2)
    return (mu_p, sigma2_p)


print m_update(mu,sigma2,nu,r2)